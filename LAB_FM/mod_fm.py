#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Modulação FM
# Author: danie
# GNU Radio version: 3.10.4.0

from packaging.version import Version as StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import analog
from gnuradio import blocks
from gnuradio import filter
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio.qtgui import Range, GrRangeWidget
from PyQt5 import QtCore
from math import pi



from gnuradio import qtgui

class mod_fm(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Modulação FM", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Modulação FM")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "mod_fm")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.f_c = f_c = 20e3
        self.samp_rate = samp_rate = 100e3
        self.k_f = k_f = 20
        self.ft = ft = 1e3
        self.fcut = fcut = f_c
        self.f_m = f_m = 1000
        self.K = K = 50

        ##################################################
        # Blocks
        ##################################################
        self._k_f_range = Range(10, 10e3, 10, 20, 200)
        self._k_f_win = GrRangeWidget(self._k_f_range, self.set_k_f, "Constante de proporcionalidade", "counter_slider", float, QtCore.Qt.Horizontal, "value")

        self.top_layout.addWidget(self._k_f_win)
        self._ft_range = Range(1e3, 40e3, 1e3, 1e3, 200)
        self._ft_win = GrRangeWidget(self._ft_range, self.set_ft, "Largura de transição do filtro passa-alta", "counter_slider", float, QtCore.Qt.Horizontal, "value")

        self.top_layout.addWidget(self._ft_win)
        self._fcut_range = Range(1e3, 50e3, 500, f_c, 200)
        self._fcut_win = GrRangeWidget(self._fcut_range, self.set_fcut, "Frequência de corte do filtro passa-alta", "counter_slider", float, QtCore.Qt.Horizontal, "value")

        self.top_layout.addWidget(self._fcut_win)
        self._K_range = Range(1, 100, 1, 50, 200)
        self._K_win = GrRangeWidget(self._K_range, self.set_K, "Amplificador", "counter_slider", float, QtCore.Qt.Horizontal, "value")

        self.top_layout.addWidget(self._K_win)
        self.qtgui_time_sink_x_3 = qtgui.time_sink_f(
            1024, #size
            samp_rate, #samp_rate
            'Saída do Filtro passa-alta', #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_3.set_update_time(0.10)
        self.qtgui_time_sink_x_3.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_3.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_3.enable_tags(True)
        self.qtgui_time_sink_x_3.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_3.enable_autoscale(False)
        self.qtgui_time_sink_x_3.enable_grid(False)
        self.qtgui_time_sink_x_3.enable_axis_labels(True)
        self.qtgui_time_sink_x_3.enable_control_panel(False)
        self.qtgui_time_sink_x_3.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_3.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_3.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_3.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_3.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_3.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_3.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_3.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_3_win = sip.wrapinstance(self.qtgui_time_sink_x_3.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_3_win)
        self.qtgui_time_sink_x_2 = qtgui.time_sink_f(
            1024, #size
            samp_rate, #samp_rate
            'Teste Integral', #name
            2, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_2.set_update_time(0.10)
        self.qtgui_time_sink_x_2.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_2.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_2.enable_tags(True)
        self.qtgui_time_sink_x_2.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_2.enable_autoscale(False)
        self.qtgui_time_sink_x_2.enable_grid(True)
        self.qtgui_time_sink_x_2.enable_axis_labels(True)
        self.qtgui_time_sink_x_2.enable_control_panel(False)
        self.qtgui_time_sink_x_2.enable_stem_plot(False)


        labels = ['Mensagem ', 'Integral da Mensagem', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(2):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_2.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_2.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_2.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_2.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_2.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_2.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_2.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_2_win = sip.wrapinstance(self.qtgui_time_sink_x_2.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_2_win)
        self.qtgui_time_sink_x_1 = qtgui.time_sink_f(
            1024, #size
            samp_rate, #samp_rate
            'Mensagem Estimada', #name
            2, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_1.set_update_time(0.10)
        self.qtgui_time_sink_x_1.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_1.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_1.enable_tags(True)
        self.qtgui_time_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1.enable_autoscale(False)
        self.qtgui_time_sink_x_1.enable_grid(False)
        self.qtgui_time_sink_x_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_1.enable_control_panel(False)
        self.qtgui_time_sink_x_1.enable_stem_plot(False)


        labels = ['Mensagem estimada', 'Mensagem Original', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(2):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_1_win = sip.wrapinstance(self.qtgui_time_sink_x_1.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_1_win)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
            1024, #size
            samp_rate, #samp_rate
            'Mensagem e Sinal', #name
            2, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(2):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.qtgui_number_sink_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_NONE,
            2,
            None # parent
        )
        self.qtgui_number_sink_0.set_update_time(0.10)
        self.qtgui_number_sink_0.set_title('Potência do sinal')

        labels = ['Potência da Mensagem', 'Potência do Sinal FM', '', '', '',
            '', '', '', '', '']
        units = ['', '', '', '', '',
            '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
            ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]

        for i in range(2):
            self.qtgui_number_sink_0.set_min(i, -1)
            self.qtgui_number_sink_0.set_max(i, 1)
            self.qtgui_number_sink_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0.set_label(i, labels[i])
            self.qtgui_number_sink_0.set_unit(i, units[i])
            self.qtgui_number_sink_0.set_factor(i, factor[i])

        self.qtgui_number_sink_0.enable_autoscale(True)
        self._qtgui_number_sink_0_win = sip.wrapinstance(self.qtgui_number_sink_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_number_sink_0_win)
        self.qtgui_freq_sink_x_1 = qtgui.freq_sink_f(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "", #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_1.set_update_time(0.10)
        self.qtgui_freq_sink_x_1.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_1.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_1.enable_autoscale(False)
        self.qtgui_freq_sink_x_1.enable_grid(False)
        self.qtgui_freq_sink_x_1.set_fft_average(1.0)
        self.qtgui_freq_sink_x_1.enable_axis_labels(True)
        self.qtgui_freq_sink_x_1.enable_control_panel(False)
        self.qtgui_freq_sink_x_1.set_fft_window_normalized(False)


        self.qtgui_freq_sink_x_1.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_1.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_1_win = sip.wrapinstance(self.qtgui_freq_sink_x_1.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_1_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_f(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            'Espectro de Frequência FM', #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        self.qtgui_freq_sink_x_0.set_fft_window_normalized(False)


        self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.low_pass_filter_0 = filter.fir_filter_fff(
            1,
            firdes.low_pass(
                1,
                samp_rate,
                5e3,
                2e3,
                window.WIN_HAMMING,
                6.76))
        self.high_pass_filter_1 = filter.fir_filter_fff(
            1,
            firdes.high_pass(
                1,
                samp_rate,
                fcut,
                ft,
                window.WIN_HAMMING,
                6.76))
        self.blocks_vco_f_0 = blocks.vco_f(samp_rate, (2*pi), 1)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_null_source_0 = blocks.null_source(gr.sizeof_float*1)
        self.blocks_multiply_xx_1 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_ff((k_f/2*pi))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff(K)
        self.blocks_moving_average_xx_0_1 = blocks.moving_average_ff(1024, ((1/1024)*(samp_rate/2/f_m)), 4000, 1)
        self.blocks_moving_average_xx_0_0 = blocks.moving_average_ff(1024, ((1/1024)), 4000, 1)
        self.blocks_moving_average_xx_0 = blocks.moving_average_ff(1024, ((1/1024)), 4000, 1)
        self.blocks_magphase_to_complex_0 = blocks.magphase_to_complex(1)
        self.blocks_correctiq_0 = blocks.correctiq()
        self.blocks_complex_to_real_0 = blocks.complex_to_real(1)
        self.blocks_add_const_vxx_0 = blocks.add_const_ff(f_c)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, f_m, 1, 0, 0)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_moving_average_xx_0_1, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.qtgui_time_sink_x_2, 1))
        self.connect((self.blocks_add_const_vxx_0, 0), (self.blocks_vco_f_0, 0))
        self.connect((self.blocks_complex_to_real_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_correctiq_0, 0), (self.blocks_complex_to_real_0, 0))
        self.connect((self.blocks_magphase_to_complex_0, 0), (self.blocks_correctiq_0, 0))
        self.connect((self.blocks_moving_average_xx_0, 0), (self.qtgui_number_sink_0, 0))
        self.connect((self.blocks_moving_average_xx_0_0, 0), (self.qtgui_number_sink_0, 1))
        self.connect((self.blocks_moving_average_xx_0_1, 0), (self.blocks_multiply_const_vxx_1, 0))
        self.connect((self.blocks_moving_average_xx_0_1, 0), (self.qtgui_time_sink_x_2, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.qtgui_time_sink_x_1, 0))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.blocks_add_const_vxx_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_moving_average_xx_0, 0))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.blocks_moving_average_xx_0_0, 0))
        self.connect((self.blocks_multiply_xx_1, 0), (self.low_pass_filter_0, 0))
        self.connect((self.blocks_multiply_xx_1, 0), (self.qtgui_freq_sink_x_1, 0))
        self.connect((self.blocks_null_source_0, 0), (self.blocks_magphase_to_complex_0, 1))
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_time_sink_x_1, 1))
        self.connect((self.blocks_vco_f_0, 0), (self.blocks_multiply_xx_0_0, 0))
        self.connect((self.blocks_vco_f_0, 0), (self.blocks_multiply_xx_0_0, 1))
        self.connect((self.blocks_vco_f_0, 0), (self.high_pass_filter_1, 0))
        self.connect((self.blocks_vco_f_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.blocks_vco_f_0, 0), (self.qtgui_time_sink_x_0, 1))
        self.connect((self.high_pass_filter_1, 0), (self.blocks_multiply_xx_1, 0))
        self.connect((self.high_pass_filter_1, 0), (self.blocks_multiply_xx_1, 1))
        self.connect((self.high_pass_filter_1, 0), (self.qtgui_time_sink_x_3, 0))
        self.connect((self.low_pass_filter_0, 0), (self.blocks_magphase_to_complex_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "mod_fm")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_f_c(self):
        return self.f_c

    def set_f_c(self, f_c):
        self.f_c = f_c
        self.set_fcut(self.f_c)
        self.blocks_add_const_vxx_0.set_k(self.f_c)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.blocks_moving_average_xx_0_1.set_length_and_scale(1024, ((1/1024)*(self.samp_rate/2/self.f_m)))
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.high_pass_filter_1.set_taps(firdes.high_pass(1, self.samp_rate, self.fcut, self.ft, window.WIN_HAMMING, 6.76))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 5e3, 2e3, window.WIN_HAMMING, 6.76))
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_1.set_frequency_range(0, self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_1.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_2.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_3.set_samp_rate(self.samp_rate)

    def get_k_f(self):
        return self.k_f

    def set_k_f(self, k_f):
        self.k_f = k_f
        self.blocks_multiply_const_vxx_1.set_k((self.k_f/2*pi))

    def get_ft(self):
        return self.ft

    def set_ft(self, ft):
        self.ft = ft
        self.high_pass_filter_1.set_taps(firdes.high_pass(1, self.samp_rate, self.fcut, self.ft, window.WIN_HAMMING, 6.76))

    def get_fcut(self):
        return self.fcut

    def set_fcut(self, fcut):
        self.fcut = fcut
        self.high_pass_filter_1.set_taps(firdes.high_pass(1, self.samp_rate, self.fcut, self.ft, window.WIN_HAMMING, 6.76))

    def get_f_m(self):
        return self.f_m

    def set_f_m(self, f_m):
        self.f_m = f_m
        self.analog_sig_source_x_0.set_frequency(self.f_m)
        self.blocks_moving_average_xx_0_1.set_length_and_scale(1024, ((1/1024)*(self.samp_rate/2/self.f_m)))

    def get_K(self):
        return self.K

    def set_K(self, K):
        self.K = K
        self.blocks_multiply_const_vxx_0.set_k(self.K)




def main(top_block_cls=mod_fm, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()

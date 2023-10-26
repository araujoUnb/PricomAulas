---
marp: true
theme: gaia
color: #000
paginate: true
footer: 'Princípios de Comunicação para Engenharia '
header: '![h:60px](../Figs/UNBS-300x150.png)'
---

<style>
    section {
          width: 1280px;
          font-size: 30px;
          padding: 40px;
          background-color: #ffffff;
    }
    section::after {
        content: 'Page ' attr(data-marpit-pagination) ' / ' attr(data-marpit-pagination-total);
        color: #000080
    }

    h1 {
       font-size: 60px ;
       color: #306030
    }

    h2 {
       font-size: 40px ;
       color: #306030
    }

    header {
        left: 29cm;
        height: 2cm;
    }

    header {
        top: 5px;
        color: #000080
    }

    footer {
     bottom: 10px;
    }

    </style>
<!-- _class: lead -->


# Resolução da Prova
Prof. Daniel Costa Araújo

---

## Questão 1

Considere o sinal $s(t)$ reescrito pela a série de Fourier

$$
\begin{align*}
    s(t)  = \frac{1}{T_p} \sum_{n=-\infty}^{\infty}g_ne^{j2\pi \frac{n}{T_p}t}
\end{align*}
$$
Considere que 
$$
\begin{align*}
    g(t) & = \Pi \left( \frac{t}{T}\right) \\
    G(f) & = T\text{sinc}\left(Tf\right)
\end{align*}
$$

---

Portanto:

$$
\begin{align*}
    s(t)  &= \frac{1}{T_p} \sum_{n=-\infty}^{\infty}G\left(f = \frac{n}{T_p}\right)e^{j2\pi \frac{n}{T_p}t} \\
         & = \frac{T}{T_p} \sum_{n=-\infty}^{\infty} \text{sinc}\left(T\frac{n}{T_p}\right)e^{j2\pi \frac{n}{T_p}t}  \\
\end{align*}
$$

Aplicando um filto em $f_p=1/T_p$ tem-se que

---

$$
\begin{align*}
    m(t)s(t)  &= m(t)\frac{T}{T_p}  \text{sinc}\left(\frac{T}{T_p}\right)e^{j2\pi \frac{1}{T_p}t} + \frac{T}{T_p}  \text{sinc}\left(\frac{T}{T_p}\right)e^{- j2\pi \frac{1}{T_p}t} \\
    &= m(t)\frac{2T}{T_p}\text{sinc}\left(\frac{T}{T_p}\right) \frac{ \left(  e^{j2\pi \frac{1}{T_p}t} + e^{- j2\pi \frac{1}{T_p}t} \right) }{2}\\
    & = m(t)\frac{2T}{T_p}\text{sinc}\left(\frac{T}{T_p}\right) \cos (2\pi f_p t)
\end{align*}
$$

---

Potência do sinal é dada por
$$
\begin{align*}
    P_u & = 2\left(\frac{T\text{sinc}\left(\frac{T}{T_p}\right)}{T_p}\right)^2 P_m \\
    \frac{P_u}{P_m} & = 2\left(\frac{T\text{sinc}\left(\frac{T}{T_p}\right)}{T_p}\right)^2 
\end{align*}
$$

---

## Questão 2

1. Cálculo de transformada de hilbert $\hat{m}(t)$

    $$
    \begin{align*}
    m(t)       & = \cos(2\pi f_m t) + 2 \sin(2\pi f_m t) \\
    \hat{m}(t) & = \sin(2\pi f_m t) - 2 \cos(2\pi f_m  t)
    \end{align*}
    $$


---

2. O sinal no tempo de banda inferior é dado por

    $$
    \begin{align*}
    u_l(t)   & = A_c m(t)\cos(2\pi f_c t) + A_c \hat{m}(t) \sin(2\pi f_c t)\\ 
            & = A_c \left[ \cos(2\pi f_m t) + 2 \sin(2\pi f_m t) \right]\cos(2\pi f_c t) \\
            &  + A_c \left[ \sin(2\pi f_m t) - 2 \cos(2\pi f_m t) \right]\sin(2\pi f_c t) \\
            & = A_c \left[ \cos(2\pi f_mt)\cos(2\pi f_c t) + \sin(2\pi f_m t)\sin(2\pi f_c t) \right] \\
            & + A_c \left[ \sin(2\pi f_m t)\cos(2\pi f_c t) -  \cos(2\pi f_m t)\sin(2\pi f_c t) \right] \\
            & = A_c \cos(2\pi (f_c - f_m) t) - 2A_c \sin(2\pi (f_c - f_m) t)
    \end{align*}
    $$

---

3. O espectro de frequência é dado por
   $$
    \begin{align*}
    u_l(t)  & = A_c \cos(2\pi (f_c - f_m) t) - 2A_c \sin(2\pi (f_c - f_m) t) \\
    U_l(f)  & = \frac{A_c}{2} \left( \delta (f - f_c + f_m) + \delta (f + f_c - f_m) \right) + A_c \jmath \left( - \delta (f - f_c + f_m) + \delta (f + f_c - f_m) \right) \\
           &= \frac{A_c}{2} \left( 1 -  2\jmath \right)\delta (f - f_c + f_m) - \frac{A_c}{2}\left( 1 + 2\jmath\right)\delta (f + f_c - f_m) \\
    |U_l(f)| & = \frac{A_c}{2} |1 -  2\jmath | +  \frac{A_c}{2} |1 +  2\jmath | \\
             & = \frac{A_c}{2} \sqrt{5}\delta (f - f_c + f_m) +  \frac{A_c}{2} \sqrt{5} \delta (f + f_c - f_m)
    \end{align*}
    $$

---

4. A potência do sinal é dada por

    $$
    \begin{align*}
        P_{u_l} & = \frac{A_c^2}{2} + \frac{4A_c^2}{2} \\
                & = \frac{5}{2}A_c^2
    \end{align*}
    $$

---

A potência do sinal DSB-AM-SC

  $$
    \begin{align*}
        P_{DSB} &= \frac{A_c^2}{2}P_m \\
                &= \frac{A_c^2}{2}\left(\frac{1}{2} + \frac{4}{2}\right) \\
                &= \frac{A_c^2}{2}\frac{5}{2}  \\
                &= \frac{5}{4}A_c^2
    \end{align*}
  $$

---

Razão de potência entre $P_{DSB}$ e $P_{u_l}$ é

   $$
    \begin{align*}
        P_{DSB}/ P_{u_l} & = \frac{5}{4}\frac{2}{5} \\
                        & = \frac{1}{2}
    \end{align*}
    $$

O custo de potência maior é da modulação SSB-AM .

---

# Questão 3

1. $f_1=1500$ Hz  e $f_2=3000$ Hz
    $$
    \begin{align*}
        m(t) & = \frac{1}{10} \cos(2\pi f_1  t) + \frac{1}{2} \cos(2\pi f_2  t) \\
        M(f) & = \frac{1}{20} \left( \delta(f - f_1) + \delta(f + f_1) \right) + \frac{1}{4}  \left( \delta(f - f_2) + \delta(f + f_2) \right)
    \end{align*}
    $$

---

2. O sinal de banda-passante é 
    $$
    \begin{align*}
        U(f) &= 10\left( \delta(f - f_c) + \delta(f + f_c) \right) + 10 M(f - f_c) + 10 M(f+f_c) \\
             & = 10\left( \delta(f - f_c) + \delta(f + f_c) \right) + \frac{1}{2}\left( \delta(f -f_c - f_1) + \delta(f - f_c + f_1) \right) + \frac{5}{2}  \left( \delta(f - f_c- f_2) + \delta(f - f_c + f_2) \right) + \\
             & \frac{1}{2}\left( \delta(f + f_c - f_1) + \delta(f + f_c + f_1) \right) + \frac{5}{2}  \left( \delta(f + f_c- f_2) + \delta(f + f_c + f_2) \right)
    \end{align*}
    $$

---

3. O cálculo do valor máximo da mensagem é

    $$
    \begin{align*}
        m^{\prime}(t) &= -\frac{2\pi f_1}{10} \sin (2\pi f_1  t) -\frac{2\pi f_2}{2} \sin (2\pi f_2  t)  \\
         &=-\frac{2\pi f_1}{10} \sin (2\pi f_1  t) - 2\pi f_2 \sin (2\pi f_1  t)\cos (2\pi f_1  t) \\
         &= -2\pi f_1 \sin (2\pi f_1  t) \left(2\cos (2\pi f_1  t) + \frac{1}{10}\right)
    \end{align*}        
    $$
    Se $m^{\prime}(t) = 0$

---

   $$
    \begin{align*}
        \cos (2\pi f_1  t) & = - \frac{1}{20} \\
        t^{\star}                  & = \frac{1}{2\pi f_1}\arccos\left( - \frac{1}{20} \right) \\
        t^{\star} & = 0.000171974 \\
        t_1^{\star} & = 0.171974 \text{ms}
    \end{align*}
    $$

---

ou 
  $$
    \begin{align*}
        \sin (2\pi f_1  t) & = 0 \\
        t_0^{\star}        & = \frac{n}{f_1}
    \end{align*}
  $$

   $$
    \begin{align*}
        m (t_0^{\star}) & = \frac{6}{10} \\
        m (t_0^{\star}) & = \frac{3}{5}
    \end{align*}
   $$


   $$
    \begin{align*}
        m (t_1^{\star}) & = -\frac{201}{400}
    \end{align*}
   $$
---

Portanto

   $$
    |m (t_0^{\star})| > |m (t_1^{\star})|
   $$
    
   $$
    \begin{align*}
        m_n(t) &= \frac{m(t)}{|m (t_0^{\star})|} \\ 
               &= \frac{5}{3}\left( \frac{1}{10} \cos(2\pi f_1  t) + \frac{1}{2} \cos(2\pi f_2  t)\right) \\
               & =\frac{1}{6} \cos(2\pi f_1  t) + \frac{5}{6} \cos(2\pi f_2  t)
    \end{align*}
   $$

   $$
    \begin{align*}
        u(t) = 20 \left[1 + \alpha m_n(t)\right]\cos(2\pi f_c t)
    \end{align*}
   $$
 Neste caso $\alpha = \frac{3}{5} = 0.6$

---


4. O relação de potência é

    $$
    \begin{align*}
        \frac{P_l}{P_c} & = \frac{20^2}{2}\alpha ^2 \frac{2}{20^2} \\
                        & = \alpha ^2 \\
                        & = \frac{9}{25} 
    \end{align*}
    $$



---

## Questão 4

$$
\begin{align*}
        X(f) = \frac{1}{B}\Pi \left( \frac{f}{B} \right) + \frac{1}{2B^2} \Delta \left(\frac{f}{B}\right) \star \Pi \left( \frac{f}{B} \right)
\end{align*}
$$

$$
\begin{align*}
    \Delta \left(\frac{f}{B}\right) \star \Pi \left( \frac{f}{B} \right) & =G_1(f) + G_2(f) + G_3(f)
\end{align*}
$$


---

$$
\begin{align*}
    G_1(f) & = \int _{-B}^{f+B/2}\left(\frac{\tau}{B} +1 \right)d\tau \,\ , -\frac{3B}{2} < f < -\frac{B}{2} \\
           & = \frac{(f+B/2)^2 - B^2}{2B} + f+\frac{B}{2} + B   \\
           & = \frac{1}{2B} \left(f^2 + Bf + \frac{B^2}{4}  - B^2 + 2Bf + B^2 + 2B^2\right) \\
           & = \frac{1}{2B} \left(f^2 + 3Bf + \frac{9B^2}{4}  \right) \\
           & = \frac{1}{2B} \left(f + \frac{3B}{2}  \right)^2 \,\ , -\frac{3B}{2} < f < -\frac{B}{2}
\end{align*}
$$

---

$$
\begin{align*}
    G_2(f) & = \int _{f - B/2}^{0}\left(\frac{\tau}{B} +1 \right)d\tau + \int _{0}^{f + B/2}\left(\frac{-\tau}{B} +1 \right)d\tau  \,\ , -\frac{B}{2} > f > \frac{B}{2} \\
    & = \left(-\frac{(f - B/2)^2}{2B}  - f + \frac{B}{2} \right) + \left(-\frac{(f + B/2)^2}{2B} + f + \frac{B}{2}  \right) \\ 
    & = -\frac{(f - B/2)^2}{2B}  -\frac{(f + B/2)^2}{2B}   + B  \\  
    & = -\frac{1}{2B} \left( 2f^2 -Bf + Bf + 2\frac{B^2}{4}  + 2B^2\right) \\
    & = -\frac{1}{B}\left( f^2 + \frac{5B^2}{4} \right) \,\ , -\frac{B}{2} < f < \frac{B}{2}
\end{align*}
$$

---

$$

\begin{align*}
    G_3(f) & = \int _{f-B/2}^{B}\left(-\frac{\tau}{B} +1 \right)d\tau \,\ , \frac{B}{2} < f < \frac{3B}{2} \\
           & = -\frac{B^2 - (f - \frac{B}{2})^2}{2B} + B - f + \frac{B}{2}   \\
           & = -\frac{1}{2B} \left( B^2 - f^2 + Bf - \frac{B^2}{4} - 2B^2 + 2Bf - B^2\right) \\
           & = \frac{1}{2B} \left(  f^2 - 3Bf + \frac{B^2}{4} + 2B^2  \right) \\
           & = \frac{1}{2B} \left(  f^2 - 3Bf + \frac{9B^2}{4} \right) \\
           & = \frac{1}{2B} \left(  f  - \frac{3B}{2} \right)^2 \,\ , \frac{B}{2} < f < \frac{3B}{2}
        
\end{align*}
$$

---

Portanto :

$$
X(f) = \begin{cases}
    \frac{1}{4B^3} \left(f + \frac{3B}{2}  \right)^2, & -\frac{3B}{2} < f < -\frac{B}{2} \\
    \frac{1}{B}-\frac{1}{2B^3}\left( f^2 + \frac{5B^2}{4} \right)  , & -\frac{B}{2} < f < \frac{B}{2} \\
    \frac{1}{4B^3} \left(  f  - \frac{3B}{2} \right)^2, & \frac{B}{2} < f < \frac{3B}{2} 
\end{cases}
$$
# [Silver IV] Time to get up! - 19025 

[문제 링크](https://www.acmicpc.net/problem/19025) 

### 성능 요약

메모리: 33432 KB, 시간: 44 ms

### 분류

구현, 문자열

### 제출 일자

2025년 2월 19일 21:43:08

### 문제 설명

<p>Little Q's alarm is ringing! It's time to get up now! However, after reading the time on the clock, Little Q lies down and starts sleeping again. Well, he has five alarms, and it's just the first one, he can continue sleeping for a while.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/d9b66f26-5dc6-44dc-8fc0-f50d34972c0c/-/preview/" style="width: 320px; height: 48px;"></p>

<p>Little Q's clock uses a standard 7-segment LCD display for all digits, plus two small segments for the "<code>:</code>", and shows all times in 24-hour format. The "<code>:</code>" segments are on at all times.</p>

<p>Your job is to help Little Q read the time shown on his clock.</p>

### 입력 

 <p>The first line of the input contains an integer <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D447 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$T$</span></mjx-container>: the number of test cases (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D447 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c34"></mjx-c><mjx-c class="mjx-c34"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>T</mi><mo>≤</mo><mn>1440</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \leq T \leq 1440$</span></mjx-container>).</p>

<p>Each test case is given on seven lines as a <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c37"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-cD7"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="3"><mjx-c class="mjx-c32"></mjx-c><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn><mo>×</mo><mn>21</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$7 \times 21$</span></mjx-container> ASCII image of the clock screen.</p>

<p>Each digit segment is represented by two characters, and each colon segment is represented by one character. Character "<code>X</code>" indicates a lit segment, character "<code>.</code>" indicates a dark segment or empty space. See the sample input for details.</p>

### 출력 

 <p>For each test case, print a single line containing a string <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D461 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$t$</span></mjx-container> formatted as "<code>HH:MM</code>": the time shown on the clock (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mtext class="mjx-ty"><mjx-c class="mjx-c1D7F6 TEX-T"></mjx-c><mjx-c class="mjx-c1D7F6 TEX-T"></mjx-c><mjx-c class="mjx-c3A TEX-T"></mjx-c><mjx-c class="mjx-c1D7F6 TEX-T"></mjx-c><mjx-c class="mjx-c1D7F6 TEX-T"></mjx-c></mjx-mtext><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D461 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mtext class="mjx-ty" space="4"><mjx-c class="mjx-c1D7F8 TEX-T"></mjx-c><mjx-c class="mjx-c1D7F9 TEX-T"></mjx-c><mjx-c class="mjx-c3A TEX-T"></mjx-c><mjx-c class="mjx-c1D7FB TEX-T"></mjx-c><mjx-c class="mjx-c1D7FF TEX-T"></mjx-c></mjx-mtext></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mtext mathvariant="monospace">00:00</mtext><mo>≤</mo><mi>t</mi><mo>≤</mo><mtext mathvariant="monospace">23:59</mtext></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$\texttt{00:00} \leq t \leq \texttt{23:59}$</span></mjx-container>).</p>


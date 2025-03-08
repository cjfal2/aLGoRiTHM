# [Silver II] Deciphering WordWhiz - 30479 

[문제 링크](https://www.acmicpc.net/problem/30479) 

### 성능 요약

메모리: 32412 KB, 시간: 44 ms

### 분류

구현, 문자열

### 제출 일자

2025년 3월 8일 09:59:19

### 문제 설명

<p>WordWhiz is a popular word puzzle game that challenges players to guess a secret word within a limited number of attempts. The game uses a dictionary containing N words. Each word in this dictionary consists of five distinct lowercase letters.</p>

<p>The game begins with the player being presented with an empty grid, consisting of a number of rows. Each row allows a single guess. The player’s task is to fill rows with words contained in the dictionary until the secret word is found, or the player has used all available rows.</p>

<p>After the player submits a guess, the game provides feedback by coloring the cells where the guess was written. The feedback consists of three colors:</p>

<ul>
	<li>Gray (“X”): The letter in the cell is not part of the secret word.</li>
	<li>Yellow (“!”): The letter in the cell is part of the secret word but is in the wrong position.</li>
	<li>Green (“*”): The letter in the cell is part of the secret word and is in the correct position.</li>
</ul>

<p>To illustrate, let’s consider the scenario where the secret word is “hotel”, and the player submits “blast” as their guess. In this case, the first, third, and fourth cells would turn gray because “b”, “a”, and “s” are not present in the secret word “hotel”. The second and fifth cells, however, would turn yellow. This indicates that “l” and “t” are part of the secret word but appear in wrong positions: “l” should be in the fifth position instead of the second, while “t” should be in the third position instead of the fifth. This feedback would be represented by “X!XX!”.</p>

<p>Now, if the player submits “heart” as their guess, the third and fourth cells would still turn gray, because “a” and “r” are not in “hotel”. The second and fifth cells would again turn yellow, because once more “t” is in the fifth position (instead of the third), and this time “e” is in the second position when it should be in the fourth. However, for this guess the first cell would turn green, indicating that “h” is the first letter in both the guess “heart” and the secret word “hotel”. This feedback would be represented by “*!XX!”.</p>

<p>Finally, if the player submits “hotel” as their guess, all cells would turn green since this is the secret word. This feedback would be represented by “*****”.</p>

<p>The feedbacks above can be seen in the following picture.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/f8b284b0-545d-482b-8011-8690f0e1d85f/-/preview/" style="width: 181px; height: 146px;"></p>

<p>Some time ago, your company added a WordWhiz player on its website and now wants to enhance the game by adding functionality to display previous game sessions. However, only the feedback for each guess was stored, not the submitted words. This means that it might not be possible to accurately recover the guesses submitted in each session, and before investing any further effort, the company wants to analyze the recorded game sessions.</p>

<p>Given a dictionary of five-letter words, the secret word (included in the dictionary) and the feedback for a game session, your task is to determine how many words in the dictionary could have been submitted as each guess.</p>

### 입력 

 <p>The first line contains an integer N (1 ≤ N ≤ 1000) indicating the number of words in the dictionary.</p>

<p>Each of the next N lines contains a string representing a word in the dictionary. All strings are different and each of them consists of five different lowercase letters. The first string is the secret word for the game session.</p>

<p>The next line contains an integer G (1 ≤ G ≤ 10) indicating the number of guesses during the game session.</p>

<p>Each of the next G lines contains a five-character string representing the feedback for a guess. The feedback string contains only the characters “X”, “!” and “*”, indicating respectively gray, yellow and green colors.</p>

<p>It is guaranteed that the input describes a valid game session.</p>

### 출력 

 <p>Output G lines, such that the i-th contains an integer indicating how many words in the dictionary could have been submitted on the i-th guess.</p>


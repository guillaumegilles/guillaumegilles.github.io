# 1 Session 1 — Sets and Combinatorial Analysis

This session introduces the language of **sets** and the main **counting techniques** used in probability.

## 1.1 Sets

### 1.1.1 Basic ideas and notation

> **NOTE:**
>
> A **set** is a collection of distinct objects called **elements** or **members**. Sets are usually written with capital letters such as \\A\\, \\B\\, or \\C\\, while elements are often written with lowercase letters such as \\a\\, \\b\\, or \\x\\.

- If an element \\x\\ belongs to a set \\A\\, we write \\x \in A\\.
- If \\x\\ does not belong to \\A\\, we write \\x \notin A\\.
- The **universal set** or **sample space** is denoted by \\\Omega\\.
- The **empty set** is denoted by \\\emptyset\\.
- A single-element set is called a **singleton**.
- A two-element set is called a **pair**.
- A subset is a part of the set.

Example: if \\A = \\\text{Finance}, \text{Marketing}, \text{HR}\\\\, then \\\text{Finance} \in A\\.

### 1.1.2 Usual sets in mathematics

- \\\mathbb{N} = \\0, 1, 2, 3, 4, \ldots\\\\ — the set of nonnegative integers
- \\\mathbb{Z} = \\\ldots, -2, -1, 0, 1, 2, \ldots\\\\ — the set of integers
- \\\mathbb{Q} = \left\\\frac{a}{b},\\ a \in \mathbb{Z},\\ b \in \mathbb{Z},\\ b \neq 0\right\\\\ — the set of rational numbers (fractions)
- \\\mathbb{R} = \]-\infty, +\infty\[\\ — the set of real numbers
- \\\mathbb{R} \setminus \\a\\\\ — the set of all real numbers except \\a\\
- \\\mathbb{R}\_+ = \[0, +\infty\[\\ — the set of nonnegative real numbers
- \\\mathbb{R}\_- = \]-\infty, 0\]\\ — the set of nonpositive real numbers

### 1.1.3 Representation of a set

- **By extension**: give an exhaustive list of all its elements.
- **By comprehension**: give a characteristic property of its elements.

For example:

- \\A = \\x \in \mathbb{N} \mid x \text{ is an even number}\\\\; by extension: \\A = \\0, 2, 4, 6, 8, \ldots\\\\
- \\B = \\x \in \mathbb{Z} \mid -2 \leq x \leq 5\\\\; by extension: \\B = \\-2, -1, 0, 1, 2, 3, 4, 5\\\\

### 1.1.4 Main operations on sets

#### Key notations

> **TIP:**
>
> For two sets \\A\\ and \\B\\:
>
> - **Inclusion**: \\A \subset B\\ means \\\forall x \in A \Rightarrow x \in B\\
> - **Union**: \\A \cup B\\ = elements in \\A\\ or \\B\\ (or both)
> - **Intersection**: \\A \cap B\\ = elements common to both sets
> - **Complement**: \\\bar{A}\\ = elements in \\\Omega\\ that are not in \\A\\
> - **Equality**: \\A = B\\ means \\\forall x,\\ x \in A \Leftrightarrow x \in B\\
>
> Note that \\A \subseteq B\\ means “\\A\\ is included in \\B\\ or equal to \\B\\”.
>
> Recall: \\A = B \Leftrightarrow A \subseteq B\\ and \\B \subseteq A\\.

Suppose in a class:

- \\A\\ = students who chose **marketing**
- \\B\\ = students who chose **finance**

Then:

- \\A \cup B\\ = students who chose marketing or finance
- \\A \cap B\\ = students who chose both
- \\\bar{A}\\ = students who did not choose marketing

### 1.1.5 Subsets and partitions

> **NOTE:**
>
> If every element of \\A\\ also belongs to \\B\\, then \\A\\ is a **subset** of \\B\\, written \\A \subset B\\.

> **NOTE:**
>
> A **partition** of \\\Omega\\ is a collection of sets that are:
>
> 1.  **Mutually exclusive**: they do not overlap,
> 2.  **Exhaustive**: together they cover all of \\\Omega\\.

> **WARNING:**
>
> Do not confuse **mutually exclusive** with **complementary**. Two sets can be disjoint without covering the whole sample space.

> **IMPORTANT:**
>
> In probability questions, start by identifying clearly:
>
> 1.  the sample space \\\Omega\\,
> 2.  the event(s) of interest,
> 3.  whether events overlap or form a partition.

Cardinal of a set : The cardinal is the size of a set. The cardinal of a finite set is the number of elements of the set. In particular, the cardinal of the empty set is zero. Notation : \|𝐸\|(or \#(𝐸), or Card(𝐸)) is the cardinal of the set 𝐸 Recall that oif 𝐴⊆𝐵, then \|𝐴\|≤\|𝐵\|; oif 𝐴⊆𝐵, then \|𝐵\|=\|𝐵\|−\|𝐴\|; oif 𝐴∩𝐵 =∅, then \|𝐴∪𝐵\|=\|𝐴\|+\|𝐵\|; o\|𝐴∪𝐵\|=\|𝐴\|+\|𝐵\|−\|𝐴∩𝐵\|; oif \|𝐴\|=𝑛, then \|𝒫(𝐴)\|=2𝑛.

## 1.2 Combinatorial analysis

The goal of **combinatorial analysis** is to count the number of elements in a finite set. he purpose of combinatorial analysis (counting techniques) is to learn how to count the number of elements in a finite set. Three techniques will be addressed: oPermutations oArrangements oCombinations These techniques depend on an operation: the factorial of a nonnegative integer.

### 1.2.1 Permutations

> **NOTE:**
>
> A **permutation** counts the number of ways to arrange **all** \\n\\ distinct objects.

> **TIP:**
>
> The number of permutations of \\n\\ distinct objects is:
>
> \\ n! = n \times (n-1) \times \cdots \times 2 \times 1 \\
>
> with the convention:
>
> \\ 0! = 1 \\

If 4 presentations must be scheduled in order, the number of possible schedules is \\4! = 24\\.

### 1.2.2 Arrangements

> **NOTE:**
>
> An **arrangement** counts the number of ways to choose and order \\k\\ objects from \\n\\ distinct objects, without repetition.

> **TIP:**
>
> The number of arrangements is:
>
> \\ A_n^k = \frac{n!}{(n-k)!} \\

If a company selects a president, a vice-president, and a treasurer from 8 candidates, the positions are different, so order matters.

### 1.2.3 Combinations

> **NOTE:**
>
> A **combination** counts the number of ways to choose \\k\\ objects from \\n\\ distinct objects when order does **not** matter.

> **TIP:**
>
> The number of combinations is:
>
> \\ C_n^k = \binom{n}{k} = \frac{n!}{k!(n-k)!} \\
>
> and it is linked to arrangements by:
>
> \\ C_n^k = \frac{A_n^k}{k!} \\

> **WARNING:**
>
> The key question is always: **does order matter?**
>
> - If yes, use permutations or arrangements.
> - If no, use combinations.

## 1.3 Detailed example

A start-up has 5 finalists for a business case competition.

### 1.3.1 Case 1: ranking all finalists

If the 5 finalists must be ranked from 1st to 5th place, we use permutations:

\\ 5! = 120 \\

### 1.3.2 Case 2: choosing 3 finalists for 3 different roles

If the roles are **speaker**, **analyst**, and **designer**, we choose and order 3 people from 5:

\\ A_5^3 = \frac{5!}{(5-3)!} = \frac{5!}{2!} = 5 \times 4 \times 3 = 60 \\

### 1.3.3 Case 3: choosing 3 finalists for the same team

If 3 people are chosen for a team and all roles are identical, we use combinations:

\\ C_5^3 = \frac{5!}{3!2!} = 10 \\

This example shows the main difference:

- **all objects used and ordered** \\\rightarrow\\ permutations,
- **some objects chosen and ordered** \\\rightarrow\\ arrangements,
- **some objects chosen without order** \\\rightarrow\\ combinations.

## 1.4 Application exercise

> **CAUTION:**
>
> A company has 10 candidates for 3 positions:
>
> 1.  In how many ways can 3 candidates be chosen if the positions are all equivalent?
> 2.  In how many ways can 3 candidates be chosen if the 3 positions are distinct (director, manager, assistant)?

> **CAUTION:**
>
> **1. Equivalent positions**
>
> Order does not matter, so we use combinations:
>
> \\ C\_{10}^3 = \frac{10!}{3! \times 7!} = \frac{10 \times 9 \times 8}{3 \times 2 \times 1} = 120 \\
>
> So there are **120 ways**.
>
> **2. Distinct positions**
>
> Order matters, so we use arrangements:
>
> \\ A\_{10}^3 = \frac{10!}{(10-3)!} = \frac{10!}{7!} = 10 \times 9 \times 8 = 720 \\
>
> So there are **720 ways**.

How many different numbers of 6digits are there oIf there are no restrictions? oIf the numbers have to be divisible by 5? oIf the repetition of digits is excluded?

The first digit cannot be 0otherwise the number would have 5digits Without any restriction One gets 9 × 10 ×10 ×10 ×10 × 10 = 900000possible numbers oIf the number ends by 0or 5(divisible by 5) One gets 9 × 10 × 10 × 10 × 10 × 2 = 180000possible numbers oIf a chosen digit cannot be re-used One gets 9 × 9 × 8 × 7 × 6 × 5 = 136080possible numbers.

## 1.5 Exercices

A padlock has three wheels, each with the digits 0to 9. How many secrets “numbers” are there?

=\> The number of possibilities is equal to 10 × 10 × 10 = 103 = 1000

From a set of 52cards, two cards are drawn simultaneously (without replacement). In how many different ways is this possible?

=\> oThe number of possibilities is equal to 10 × 10 × 10 = 103 = 1000 oIt corresponds to the number of different ways you can choose a pair of cards from a deck of 52cards, that is 𝐶522 =1326

The code on your laptop is made up of 4numbers (ranging from 0 to 9each). A criminal has observed you doing the code. He managed to see only one number (but he doesn’t remember its position). What is the (maximum) number of tries for the criminal to unlock your laptop?

=\> First, the number of possible ways one can place the known digit is equal to 𝐶41 =4 And then, the number of possibilities for the remaining three digits is equal to 10 × 10 × 10 = 103 = 1000. Thus the (maximum) number of tries is equal to 4 × 1000 = 4000.

## 1.6 Quizz

Question 1 A code has five elements: three digits and two letters If the digits of the code are distinct, then the total number of possible codes is equal to : • 20 x 10 x 9 x 8 x 26 x 26 • **10 x 10 x 9 x 8 x 26 x 26** • 10 x 10 x 9 x 8 x 26 x 25 • 10 x 9 x 8 x 7 x 26 x 26 Feedback: We multiply the number of possibilities to place the 2 letters (therefore the 3 digits) among 5 positions: 𝐶52 = 𝐶53 =10, by the number of arrangements without repetition of 3 (distinct) digits 10x9x8 by the number of arrangements with repetition of 2 letters 26x26

Question 2 A code has five elements: three digits and two letters If the code begins with the digit 0, then the total number of possible codes is equal to : • 26 x 26 x 10 x 10 • 10 x 26 x 25 x 10 x 9 • **6 x 26 x 26 x 10 x 10** • 10 x 26 x 25 x 10 x 9 Feedback: If the code starts with 0, there are 2 numbers and 2 letters left to place. We multiply the number of possibilities to place the 2 letters (therefore the 2 digits) among 4 positions: 𝐶42 =6, by the number of arrangements with repetition of 2 digits 10x10 by the number of arrangements withrepetition of 2 letters 26x26

Question 3 A code has five elements: three digits and two letters If the code begins with the letter A, then the total number of possible codes is equal to : • 26 x 10 x 10 x 10 • 26 x 26 x 10 x 10 • **4 x 26 x 10 x 10 x 10** • 26 x 10 x 9 x 8 Feedback: If the code begins with A, there are 1 letter and 3 numbers left to place. We multiply the number of possibilities to place the letter (therefore the 3 digits) among 4 positions: 𝐶41 = 𝐶43 =4, by the number of possible letters 26 by the number of arrangements with repetition of 3 digits 10x10x10

Question 4 A code has five elements: three digits and two letters If the code begins with two letters, then the total number of possible codes is equal to : • 26 x 25 x 10 x 9 x 8 • 26 x 25 x 10 x 10 x 10 • **26 x 26 x 10 x 10 x 10** • 26 x 26 x 10 x 9 x 8 Feedback: If the code begins with 2 letters, the positions of the 2 letters and the 3 digits are imposed. We just multiply the number of arrangements with repetition of 2 letters 26x26 by the number of arrangements with repetition of 3 digits 10x10x10

Question 5 A code is made up of two digits and two letters of the alphabet in all possible orders. Thus, we can deduce that if the digits of the code are distinct, then the total number of possible codes is equal to: • 10 x 9 x 26 x 26 • **6 x 10 x 9 x 26 x 26** • 12 x 10 x 9 x 26 x 26 • 4 x 10 x 9 x 26 x 26 Feedback: We multiply the number of possibilities to place the 2 letters (therefore the 2 digits) among 4 positions: 𝐶42 =6, by the number of arrangements without repetition of 2 (distinct) digits 10x9 by the number of arrangements with repetition of 2 letters 26x26

Question 6 A code is made up of two digits and two letters of the alphabet in all possible orders. Thus, we can deduce that if the code begins with the number 0, then the total number of possible codes is equal to: • 10 x 26 x 26 • 2 x 10 x 26 x 26 • **3 x 10 x 26 x 26** • 4 x 10 x 26 x 26 Feedback: If the code starts with 0, there are 1 digits and 2 letters left to place. We multiply the number of possibilities to place the digit (therefore the 2 letters) among 3 positions: 𝐶31 𝐶32 =3, by the number of possible digits: 10 by the number of arrangements with repetition of 2 letters : 26x26

Question 7 A code is made up of two digits and two letters of the alphabet in all possible orders. Thus, we can deduce that if the code begins with the letter A, then the total number of possible codes is equal to : • 26 x 10 x 10 x 2 • **26 x 10 x 10 x 3** • 26 x 10 x 10 x 4 • 26 x 10 x 10 x 6 Feedback: If the code begins with A, there are 1 letter and 2 numbers left to place. We multiply the number of possibilities to place the letter (therefore the 2 digits) among 3 positions: 𝐶31 = 𝐶32 = 3, by the number of possible letters 26 by the number of arrangements with repetition of 2 digits 10x10

Question 8 A code is made up of two digits and two letters of the alphabet in all possible orders. Thus, we can deduce that if the code starts with two letters, then the total number of possible codes is equal to : • 26 x 25 x 10 x 10 • **26 x 26 x 10 x 10** • 26 x 25 x 10 x 9 • 26 x 26 x 10 x 9 Feedback: If the code starts with 2 letters, the positions of the 2 letters and the 2 digits are imposed. We just multiply the number of arrangements with repetition of 2 letters 26x26 by the number of arrangements with repetition of 2 digits 10x10

# SequenceAlignmentProblem

![image](https://github.com/koushikreddykonda/SequenceAlignmentProblem/assets/122440945/48ddb3be-3914-407f-8372-cc568cb2052c)


 ![image](https://github.com/koushikreddykonda/SequenceAlignmentProblem/assets/122440945/fe521fc9-d68f-4b79-93b1-86510500353d)
 
Insights

<img width="922" alt="Screenshot 2023-09-07 at 9 36 03 PM" src="https://github.com/koushikreddykonda/SequenceAlignmentProblem/assets/122440945/5e86a2cd-0037-4b73-830c-9b0698fbc073">



Nature of the Graph (Logarithmic/ Linear/ Polynomial/ Exponential) 
Basic: Polynomial Efficient: Linear Explanation:  
From the graph, we can see that when the input sizes are small, there’s no big difference in memory consumption of basic and efficient algorithm. However when the input size grows, the basic algorithm takes more memory – O(m*n) as we maintain the costs for every conceivable alignment whereas in the efficient algorithm, the memory remains same because we use only limited – 2 columns for computing the cost, here we partition the first string from the middle part and by looking at each index of the second string to divide and selecting the one that provides the lowest cost. Therefore, memory in efficient algorithm is linear while it is polynomial in basic.
 
<img width="878" alt="Screenshot 2023-09-07 at 9 36 20 PM" src="https://github.com/koushikreddykonda/SequenceAlignmentProblem/assets/122440945/892429be-8cae-4f34-8b11-055ce61caf72">



Nature of the Graph (Logarithmic/ Linear/ Polynomial/ Exponential) 
Basic: Polynomial Efficient: Polynomial Explanation:  
For small input sizes, the time taken by basic and efficient algorithm is nearly same. Whereas as the input size increases, memory efficient algorithm takes more time to compute the cost where as basic algorithm take less time to compute the result. For memory efficient algorithm we divide the first string from the middle, and then we locate the division point of the second string by looking at every index to divide, and then selecting the index which returns the lowest cost. Here, the time taken for this process is polynomial, plus time for stack maintenances. Coming to basic algorithm, a 2-D matrix is being maintained to determine the cost of all possible combinations in strings backtracking is used to get the exact sequence alignment in this process of cost calculation 2 nested for loops are used the thus time taken is polynomial.



# HashCode2020
 This is a repository containing codes of [UCD](https://www.ucd.ie/) at HashCode 2020

#### [Practice-V1](practice/v1.py): First version on HashCode pratice
- The method we used is exhaustive
- Hence, the complexity is very high. For example, for the medium sample, it takes 2e50 times of search, that is unrealistic for the actual problem
- We need to consider optimization solutions

### [Practice-V2](practice/v2.py): Second version on HashCode pratice
- We first shuffle the original slices type list K=10000 times with different random seeds, so we get K randomlized lists. 
- Then apply the maximum sum segment algorithm for the K lists
- Next, get maximum segment out of the K maximum sum segments 
- The algorithm does not guarantee the optimal but intuitively come close to the optimal
- Assume the length of original list is N, the algorithm's complexity is O(N*K) that is efficient for the problem 
- Finally We achieve a total score of 1,505,004,615 on Hashcode [Judge System](https://hashcodejudge.withgoogle.com/)
- This result is very promising and pleasing!

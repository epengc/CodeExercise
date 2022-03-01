# P13. Force Recursion Example
## 1. Hanoi Tower
The classic Hanoi Tower case is that where there are three bars such as "From", "Other" and "To", the multi-layers plates in "From" bar should be moved to "To" bar. The main idea for solution is that if we call the plate on the top is the $1^{st}$ plate and on the bottom is the $N^{th}$ plate. 

![hanoi1](/assets/hanoi1.png)

If the plates from $1^{st}$ to $(N-1)^{st}$ are regarded as one part and the last $N^{st}$ plate is seen as the other part, then, we can separate the whole task into 3 steps. The $1^{st}$ step is moving the $1^{st}$ $\sim$ $(N-1)^{st}$ part from "From" bar to "Other" bar. 

![hanoi2](/assets/hanoi2.png)

The $2^{nd}$ Step is to move the $N^{th}$ plate from the "From" bar to "To" bar directly. 

![hanoi3](/assets/hanoi3.png)

The $3^{rd}$ Step is to move the $1^{st}$ $\sim$ $(N-1)^{st}$ part from the "Other" bar to "To" bar.

![hanoi4](/assets/hanoi4.png)

It is the general percedure of hanoi tower moving task. The one key issue would be mentioned here is in the $1^{nd}$ step, if we want to move the $1^{st}$ $\sim$ $(N-1)^{st}$ part from the "From" bar to "Other" bar, the "Other" bar could play the role as "To" bar. Meanwhile the "To" bar plays its role of "Other" bar. The same thing happens in the $3^{rd}$ step. In the $3^{rd}$ step, when we want to move the $1^{st}$ $\sim$ $(N-1)^{st}$ part from "Other" bar to "To" bar, this time, the "Other" bar plays its role as "From" bar and the "From" bar takes its role as "Other" bar.

So if structuring the Hanoi Tower's recursive task, we would code like this:
```cpp
    void hanoi(int N, string From, string To, string Other){
        if(N==1){
            cout<<"Move the 1 plate from the "<< From<<" bar to "<<To<<" bar“<<endl;
        }
        hanio(N-1, From, Other, To);
        cout<<"Move the "<<N<<" th plate from the "<<From<<" bar to the "<< To<<" bar"<<endl;
        hanio(N-1, Other, To, From);
    }
```


# let's see the selection sort algoritham 


#-------------------------------------------------------------------
# lets try to implement insertion sort sort inorder to sort the array element 
def insertion_sort(array):
     
     for i in range(1,len(array)):
           tamp=array[i]
           print(i,end=" ")
           j=i-1
           while j >= 0 and array[j] > tamp:
               array[j+1]= array[j]
               j-=1
           array[j+1]= tamp ; 

     return array 
           



#-------------------------------------------------------------------------
#this code for sorting the  array element 
def selectionsort(array):
     for i in range(len(array)) :
          min_idx=i
          # lets' try to find next smaller element 
          for j in  range(i+1, len(array)):
               if array[min_idx]> array[j]:
                     min_idx= j
         # lets' swap  here  this 
          t= array[min_idx]
          array[min_idx]= array[i]
          array[i]= t 
     return array
#this code for reversing the string word by word . 
#-------------------------------------------------------------------
def reverserthestring(S):
     string=S.split(".")
     ans=""
     for word in string[::-1]:
          ans+="."+word 
     return ans[1::]
#----------------------------------------------------------------------------
#here again the same code   have wriiten for sorting the array element but  this time it is used recrusion techinque  . 
def selectionsortUsingrec(array,  index ):
           if index  ==  len(array)-1:
               return 
           k=index  
               # lets's the  play the game of  sorting algorithms .
           for j in range(k+1, len(array)):
               if( array[index] > array[j]):
                    index=j
          # let's the swap the value 
          # in the python we have to very care about indentation  . 
           t= array[index]
           array[index]= array[k]
           array[k]= t 
           selectionsortUsingrec(array, k+1)
  #---------------------------------------------------------------------------  
  # lets' implement merge sort using python 

# thsi code is for merge sort but why I am not able  to apply on array list in the python . 

def mergethem(array, start, mid, end):
     arraytamp=[]
     j=mid+1
     s=start
     k=0
     while s<=mid and j<= end :
          if array[s] >= array[j]:
               arraytamp.insert(k,array[j])
               k+=1
               j+=1
          else:
                arraytamp.insert(k,array[j])
                s+=1
                k+=1
     while s<=mid :
          arraytamp.insert(k,array[s])
          s+=1
          k+=1
     while( j<= end):
           arraytamp.insert(k,array[j])
           k+=1
           j+=1

     
     array=arraytamp
     print(array)
def mergesort(array, start , end):
          if(start<end):
                mid=(start+end) // 2
                mergesort(array, start, mid)
                mergesort(array, mid+1, end)
                mergethem(array, start, mid, end)

            # return ; #this will be our base
            


          
 #-----------------------------------------------------------------------------#
# inside the this lair we are calling the all the function which we have difined over there .          
# let's call this function
#s='i.like.this.program.very.much'
#st=reverserthestring(s)
#print(st)
array=[12,34,56,76,-68,33,245,7,0]
a=[]
#a=array
#print(a)
#print(len(array))
mergesort(array,0,len(array)-1)
print(array, end=" ")

#-------------------------------------------------------------------------------#
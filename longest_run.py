def longest_run(L):

   longest_run_decrease_count=1
   
   decrease_start=0
   longest_run_decrease_start=0
   longest_run_increase_count=1
   longest_run_increase_start=0
   increase_count=1
   increase_start=0
   for i in range(len(L)-1):
     if L[i] >= L[i+1]:
       
       decrease_start = i
       decrease_count=1
       for j in range(i, len(L)-1):
           if L[j] >= L[j+1]:
               decrease_count += 1
               
           else:
               break
       if decrease_count > longest_run_decrease_count:
           longest_run_decrease_count = decrease_count
           longest_run_decrease_start = decrease_start
           
                
     if L[i]<=L[i+1]:
       
       increase_start = i
       increase_count=1
       for j in range(i, len(L)-1):
           if L[j] <= L[j+1]:
               increase_count += 1
               
           else:
               break
       if increase_count > longest_run_increase_count:
           longest_run_increase_count = increase_count
           longest_run_increase_start = increase_start
   #print(L[longest_run_decrease_start:longest_run_decrease_start+longest_run_decrease_count])
   #print(longest_run_decrease_start)
   #print(L[longest_run_increase_start:longest_run_increase_start+longest_run_increase_count])
   #print(longest_run_increase_start)
   if len(L[longest_run_increase_start:longest_run_increase_start+longest_run_increase_count]) > len(L[longest_run_decrease_start:longest_run_decrease_start+longest_run_decrease_count]):
      return sum(L[longest_run_increase_start:longest_run_increase_start+longest_run_increase_count])
   elif len(L[longest_run_increase_start:longest_run_increase_start+longest_run_increase_count]) < len(L[longest_run_decrease_start:longest_run_decrease_start+longest_run_decrease_count]):
      return sum(L[longest_run_decrease_start:longest_run_decrease_start+longest_run_decrease_count])
   else:
      if longest_run_increase_start < longest_run_decrease_start:
         return sum(L[longest_run_increase_start:longest_run_increase_start+longest_run_increase_count])
      else:
         return sum(L[longest_run_decrease_start:longest_run_decrease_start+longest_run_decrease_count])
         
   


    
        

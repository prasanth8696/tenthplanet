import java.util.*;


public class Expense implements Comparable<Expense> {
        private String category ;
	private int amount;

	public Expense(){


         }
        public Expense(String category,int amount){
		this.category = category;
		this.amount = amount;
        }

        //getter
        public String getCategory(){
		return this.category;
       }
       //setter
       public void setCategory(String category){
		this.category = category;
       }

       //getter
        public int getAmount(){
                return this.amount;
       }
       //setter
       public void setAmount(int amount){
                this.amount = amount;
       }

      public int compareTo(Expense ob){
	return (this.amount - ob.amount);
      }





}

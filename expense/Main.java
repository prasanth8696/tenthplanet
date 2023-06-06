import java.util.Scanner;
import java.util.TreeSet;
import java.util.Iterator;
public class Main{

	public static void main(String[] args){
		TreeSet<Expense> expenses = new TreeSet<>();

		Scanner sc = new Scanner(System.in);

		while(true){
			System.out.println("Enter expense Category ");
			String category = sc.next();
			System.out.println("Enter expense Amount ");
			int amount = sc.nextInt();

			expenses.add(new Expense(category,amount));
		        System.out.println("Do you want to continue?yes/no");
			String in = sc.next().toLowerCase();
			if(in.equals("yes"))
				continue;
  			else if(in.equals("no"))
				break;
			else 
				System.out.println("Invalid input...");
		}

    		Iterator<Expense> it = expenses.descendingIterator();
		int total_amount = 0;

		System.out.println("Category           Amount");
		while(it.hasNext()){
			Expense expense = it.next();
                        System.out.println(expense.getCategory() + "           " + expense.getAmount());
                        total_amount += expense.getAmount();
		}
		

	
	
	
	}


}

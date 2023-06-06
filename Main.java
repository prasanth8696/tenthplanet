import java.util.Scanner;
import java.util.ArrayList;
import java.util.HashSet;
public class Main{
	static HashSet<User> userSet = new HashSet<User>();
	static ArrayList<User> userList = new ArrayList<User>();
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter no of users :");
		int n = sc.nextInt();
		for (int i=0;i<n;i++){
			System.out.println("Enter details of User " + (i+1));
			System.out.println("Username:");
			String username = sc.next();
			System.out.println("Bank Name:");
			String bankname = sc.next();
			userSet.add(new User(username,bankname));
		}
		System.out.println("Enter username(Expire in one month)\nseperatedby comma(CSV FORMAT)");
		String[]  userNameList = sc.next().split(",");
		for(String username : userNameList ){
			userList.add(new User(username,null));
		}
                retainAll();

		//print the output
		int count = 1;
		System.out.println("Users going to expire within a month...");
		for(User user : userSet){
			System.out.println("User " + count);
			System.out.println("User Name = " + user.getUserName());
			System.out.println("Bank Name = " + user.getBankName());
			count++;
		}
	
	}

	public static void retainAll(){
		for( User setUser : userSet){
                        boolean activeUser = true;
			for(User listUser : userList){
				if (setUser.equals(listUser)){
					activeUser = true;
					break;
				}
				else{
					activeUser = false;
				}
			}
			if(activeUser == false)
				userSet.remove(setUser);

		}

	}

}      

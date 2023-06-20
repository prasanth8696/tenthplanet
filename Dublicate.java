import java.util.Scanner;
import java.util.ArrayList;


public class Dublicate {

	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		ArrayList<String> usernames = new ArrayList<>();
		int n = sc.nextInt();

		for(int i=0;i<n;i++){
			usernames.add(sc.next());
		}
                String search_username = sc.next();
		int count = 0;
		for(String username : usernames){
			if(username.equals(search_username))
				count++;
		}

		System.out.println(count);


	}

}

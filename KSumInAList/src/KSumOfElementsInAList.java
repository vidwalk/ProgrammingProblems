import java.util.ArrayList;
import java.util.List;

public class KSumOfElementsInAList {
	/**
	 * This problem was recently asked by Google(1/05/2019).
	 * 
	 * Given a list of numbers and a number k, return whether any two numbers from
	 * the list add up to k.
	 * 
	 * For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is
	 * 17.
	 * 
	 * Bonus: Can you do this in one pass?
	 * 
	 * @param k
	 * @param list
	 * @return
	 */
	public static boolean kSumInAList(int k, ArrayList<Integer> list) {
		// Easiest and most obvious method. Not the best
		for(int i = 0; i < list.size() - 1; i++)
			for(int j = 1; j< list.size(); j++)
			{
				if(list.get(i) + list.get(j) == k)
					return true;
			}
		return false;
	}

	public static void main(String[] args) {
		var list = new ArrayList<>(List.of(10, 15, 3, 7));
		var k = 17;

		if (kSumInAList(k, list))
			System.out.println("K was found as a sum of two elements in the list");
		else
			System.out.println("K wasn't found as a sum of two elements");
	}

}

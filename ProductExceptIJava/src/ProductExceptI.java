import java.util.ArrayList;
import java.util.List;

public class ProductExceptI {

	/**
	 * This is your coding interview problem for today.
	 * 
	 * This problem was asked by Uber.
	 * 
	 * Given an array of integers, return a new array such that each element at
	 * index i of the new array is the product of all the numbers in the original
	 * array except the one at i.
	 * 
	 * For example, if our input was [1, 2, 3, 4, 5], the expected output would be
	 * [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would
	 * be [2, 3, 6].
	 * 
	 * Follow-up: what if you can't use division?
	 * @param list
	 * @return
	 */
	private static ArrayList<Integer> productExceptI(ArrayList<Integer> list) {
		ArrayList<Integer> result = new ArrayList<Integer>();
		for (int i = 0; i < list.size(); i++) {
			int product = 1;
			for (int j = 0; j < list.size(); j++)
				if (i != j)
					product = product * list.get(j);
			result.add(product);
		}

		return result;
	}

	public static void main(String[] args) {

		var list = new ArrayList<Integer>(List.of(1, 2, 3, 4, 5));
		System.out.println(productExceptI(list).toString());
	}
}

import java.util.ArrayList;
import java.util.List;

/**
 * 
 */

/**
 * @author Claudiu
 *
 */
public class FindSmallestPosInt {

	/**
	 * This problem was asked by Stripe.
	 * 
	 * Given an array of integers, find the first missing positive integer in linear
	 * time and constant space. In other words, find the lowest positive integer
	 * that does not exist in the array. The array can contain duplicates and
	 * negative numbers as well.
	 * 
	 * For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0]
	 * should give 3.
	 * 
	 * You can modify the input array in-place.
	 * 
	 * @param list
	 * @return
	 */
	public static int findSmallestPosInt(ArrayList<Integer> list) {
		var min = 999999;
		for (int number : list) {
			if (number >= 0 && number < min)
				min = number;
		}
		min += 1;
		for (int number : list) {
			if (number == min)
				min = number + 1;
		}
		return min;
	}

	public static void main(String[] args) {
		var list = new ArrayList<Integer>(List.of(3, 4, -1, 1));
		var list1 = new ArrayList<Integer>(List.of(1, 2, 0));
		System.out.println(findSmallestPosInt(list));
		System.out.println(findSmallestPosInt(list1));
	}

}

import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = Integer.parseInt(sc.nextLine());
        String[] input = sc.nextLine().split(" ");
        int[] fruits = new int[n];
        for (int i = 0; i < n; i++) {
            fruits[i] = Integer.parseInt(input[i]);
        }

        Map<Integer, Integer> fruit_cnt = new HashMap<>();
        int left = 0;
        int max_len = 0;

        for (int right = 0; right < n; right++) {
            fruit_cnt.put(fruits[right], fruit_cnt.getOrDefault(fruits[right], 0) + 1);

            while (fruit_cnt.size() > 2) {
                fruit_cnt.put(fruits[left], fruit_cnt.get(fruits[left]) - 1);
                if (fruit_cnt.get(fruits[left]) == 0) {
                    fruit_cnt.remove(fruits[left]);
                }
                left++;
            }

            max_len = Math.max(max_len, right - left + 1);
        }

        System.out.println(max_len);
    }
}

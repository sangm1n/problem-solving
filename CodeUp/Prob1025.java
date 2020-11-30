/*
다섯 자리의 정수 1개를 입력받아 각 자리별로 나누어 출력한다.
 */

import java.util.*;

public class Prob1025 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        String input = scan.nextLine();
        String[] arr = input.split("");
        int[] arr2 = new int[arr.length];

        int[] idx = {10000, 1000, 100, 10, 1};
        for (int i = 0; i < arr2.length; i++) {
            arr2[i] = Integer.parseInt(arr[i]);
            System.out.println("[" + arr2[i] * idx[i] + "]");
        }
    }
}

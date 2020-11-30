/*
어떤 형식에 맞추어 시간이 입력될 때, 그대로 출력하는 연습을 해보자.
 */

import java.util.*;

public class Prob1018 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        String input = scan.nextLine();
        String[] arr;
        arr = input.split(":");
        int[] arr2 = new int[arr.length];

        for (int i = 0; i < arr.length; i++) {
            arr2[i] = Integer.parseInt(arr[i]);
            System.out.print(arr2[i] + " ");
        }
    }
}

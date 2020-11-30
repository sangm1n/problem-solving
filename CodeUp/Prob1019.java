/*
년, 월, 일을 입력받아 지정된 형식으로 출력하는 연습을 해보자.
 */

import java.util.*;

public class Prob1019 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        String input = scan.nextLine();
        String[] arr = input.split("\\.");
        int[] arr2 = new int[arr.length];

        for (int i = 0; i < arr2.length; i++) {
            arr2[i] = Integer.parseInt(arr[i]);
        }

        System.out.printf("%d.%02d.%02d", arr2[0], arr2[1], arr2[2]);
    }
}

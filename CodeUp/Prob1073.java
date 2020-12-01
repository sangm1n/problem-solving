/*
정수가 순서대로 입력된다.
-2147483648 ~ +2147483647, 단 개수는 알 수 없다.

0이 아니면 입력된 정수를 출력하고, 0이 입력되면 출력을 중단해보자.
 */

import java.util.Scanner;

public class Prob1073 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        String input = scan.nextLine();
        String[] arr = input.split(" ");

        for (int i = 0; i < arr.length; i++) {
            if (Integer.parseInt(arr[i]) == 0) {
                break;
            }
            System.out.println(Integer.parseInt(arr[i]));
        }
    }
}

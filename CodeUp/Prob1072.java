/*
n개의 정수가 순서대로 입력된다.
-2147483648 ~ +2147483647, 단 n의 최대 개수는 알 수 없다.

n개의 입력된 정수를 순서대로 출력해보자.
 */

import java.util.Scanner;

public class Prob1072 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int num = scan.nextInt();

        for (int i = 0; i < num; i++) {
            int number = scan.nextInt();
            System.out.println(number);
        }
    }
}

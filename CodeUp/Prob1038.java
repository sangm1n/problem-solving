/*
정수 2개를 입력받아 합을 출력하는 프로그램을 작성해보자.
(단, 입력되는 정수는 -1073741824 ~ 1073741824 이다.)
 */

import java.util.Scanner;

public class Prob1038 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        long a = scan.nextLong();
        long b = scan.nextLong();

        System.out.println(a+b);
    }
}

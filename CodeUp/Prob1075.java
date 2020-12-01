/*
정수(1 ~ 100) 1개가 입력되었을 때 카운트다운을 출력해보자.
1씩 줄이면서 한 줄에 하나씩 0이 될 때까지 출력한다.
 */

import java.util.Scanner;

public class Prob1075 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int num = scan.nextInt();

        for (int i = num-1; i >= 0; i--) {
            System.out.println(i);
        }
    }
}

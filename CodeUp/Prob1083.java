/*
3 6 9 게임을 하던 영일이는 3 6 9 게임에서 잦은 실수로 계속해서 벌칙을 받게 되었다.
3 6 9 게임의 왕이 되기 위한 마스터 프로그램을 작성해 보자.
 */

import java.util.Scanner;

public class Prob1083 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int num = scan.nextInt();
        for (int i = 1; i <= num; i++) {
            if (i % 3 == 0)
                System.out.print("X" + " ");
            else
                System.out.print(i + " ");
        }
    }
}

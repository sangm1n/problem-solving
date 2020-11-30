/*
정수형(int)으로 변수를 선언하고, 변수에 정수값을 저장한 후
변수에 저장되어 있는 값을 그대로 출력해보자.
 */

import java.util.*;

public class Prob1010 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        String input = scan.nextLine();
        int num = Integer.parseInt(input);
        System.out.println(num);
    }
}

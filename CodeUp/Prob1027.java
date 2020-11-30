/*
년월일을 출력하는 방법은 나라마다, 형식마다 조금씩 다르다.

년월일(yyyy.mm.dd)를 입력받아,

일월년(dd-mm-yyyy)로 출력해보자.

(단, 한 자리 일/월은 0을 붙여 두자리로, 년도도 0을 붙여 네자리로 출력한다.)
 */

import java.util.*;

public class Prob1027 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        String input = scan.nextLine();
        String[] arr = input.split("\\.");
        int[] arr2 = new int[arr.length];

        for (int i = 0; i < arr2.length; i++) {
            arr2[i] = Integer.parseInt(arr[i]);
        }

        System.out.printf("%02d-%02d-%04d%n", arr2[2], arr2[1], arr2[0]);
    }
}

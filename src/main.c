#include <stdio.h>

#include "banner.h"
#include "calc.h"
#include "hello.h"

int main(void) {
    int left = 2;
    int right = 3;
    int result = add_numbers(left, right);

    print_banner("WSL Test App");
    printf("%s\n", get_greeting());
    printf("%d + %d = %d\n", left, right, result);

    return 0;
}

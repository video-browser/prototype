#include <stdio.h>
#include <iostream>
#include <boost/lambda/lambda.hpp>

int main() {
  printf("123\n");
  using namespace boost::lambda;
  typedef std::istream_iterator<int> in;

  std::for_each(
      in(std::cin), in(), std::cout << (_1 * 3) << " " );
  return 0;
}

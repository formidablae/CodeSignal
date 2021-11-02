boolean isoscelesTriangle(int[] sides)
{
    int a = sides[0];
    int b = sides[1];
    int c = sides[2];
    
    /*if (a + b <= c || a + c <= b || b + c <= a || a <= 0 || b <= 0 || c <= 0) return false;
    else */if (a == b || a == c || b == c) return true;
    else return false;
}

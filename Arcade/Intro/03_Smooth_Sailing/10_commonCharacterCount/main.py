def commonCharacterCount(s1, s2):
    count = 0;
    found = True;
    i = 0;
    while (i < len(s1)):
        found = False;
        print("entered outer while");
        j = 0;
        while ((j < len(s2)) and (i < len(s1))):
            print("entered inner while");
            if s1[i] == s2[j]:
                print("entered if");
                count += 1;
                if (i < len(s1) - 1):
                    s1 = s1[0:i] + s1[i + 1: len(s1)];
                else:
                    s1 = s1[0:i];
                
                if (j < len(s2) - 1):
                    s2 = s2[0:j] + s2[j + 1: len(s2)];
                else:
                    s2 = s2[0:j];
                
                found = True;
                print("found");
                print("i = " + str(i));
                print("new s1 = " + s1);
                print("new s2 = " + s2);
            else:
                j += 1;
                print("not found");
                print("i = " + str(i));
                print("j = " + str(j));
        if (not found):
            i += 1;
            print("new i = " + str(i));
        else:
            print("same i = " + str(i));
    return count;
    
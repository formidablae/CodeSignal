String[] addBorder(String[] picture)
{
    String[] newPicture = new String[picture.length + 2];
    newPicture[0] = "";
    newPicture[newPicture.length - 1] = "";
        
    for (int i = 0; i < picture[0].length() + 2; i++)
    {
        newPicture[0] = newPicture[0] + "*";
        newPicture[newPicture.length - 1] = newPicture[newPicture.length - 1] + "*";
    }
    
    for (int i = 0; i < picture.length; i++)
    {
        newPicture[i + 1] = "*" + picture[i] + "*";
    }
    
    return newPicture;
}

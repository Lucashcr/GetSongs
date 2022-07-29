#include <iostream>
#include <string>
#include <unistd.h>

int main(int argc, char* argv[]) 
{
    char path[256];
    getcwd(path, 256);
    std::string path_str = std::string(path);

    std::string interp = path_str + "/venv/Scripts/python.exe";
    std::string main_file = path_str + "/main.py";
    std::string command = interp + " " + main_file;

    if (argc > 1)
    {
        command += " " + static_cast<std::string>(argv[1]);
    }

    system(command.c_str());

    return 0;
}

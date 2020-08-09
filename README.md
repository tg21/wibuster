# WiBuster
A Website enumerator that can tackle wild card response. \
currently is only functional enough to show that it is possible. 


### It is programmed in python3
It can enumerate web servers that send response code 200 even when the file is not present.

### whats new ?
 - Enabled Multi Threading
 - Now file extenstions are accepted for enumeration
 - host, extentions, dictionary and thread count are accepted as Command line arguments

### usage
```shell
    python3 wibuster.py <host> <extentions> <path_to_dictionary> <thread_count>
    
    # for help use
    python3 wibuster.py -h
```
### example
```shell
    python3 wibuster.py http://localhost ".html .php" dictionary-list-1.0.txt 10
```
## TODOs
 - Add multithreading for faster process. ✅ done
 - Add features to enumerate with file extentions. ✅ done
 - add command line arguments options. ✅ done

### Development

Want to contribute? Great!
Help is always welcome.

License
----

It has none.(what is this deal with all license stuff and how do I get one?)


**Free Software, yeah enjoy!**
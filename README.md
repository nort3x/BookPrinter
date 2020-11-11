# BookPrinter
a handy script for printing MultiplePages PDF (books and documents) double sided , with simple printers


* ##   instructions for Generation:
    * ### on Linux:
       * install if not already installed : ``` pdfseperate , pdfunite, python3```
       * use the script to generate top and bottom: ``` python3 BookPrinter.py --input /path/to/book.pdf -f 10 -l 100``` will generate for 10-100 pages
       * print top and bottom with next set of instructions
    
    * ### on Windows:
       * not tested 
       
      
---------------
      
* ##   instructions for Printing:
    * the goal is to print top.pdf then complete it with bot.pdf so we can bind it to a book

    * ### Right to left Languages:
       * print ```top.pdf``` on ```potrait mode``` and ```all sheets``` and ```two pages per side``` , ```Right to Left```
       * ![alt text](https://github.com/nort3x/BookPrinter/blob/main/img/conf.png)
       * re-print ```bot.pdf``` on ```potrait mode``` and ```all sheets``` and ```two pages per side``` , ```Left to Right``` on the other side of paper
       * bind them together:
       * ![alt text](https://github.com/nort3x/BookPrinter/blob/main/img/r2l.png)
    
    * ### Left to Right Languages:
       * print ```top.pdf``` on ```potrait mode``` and ```all sheets``` and ```two pages per side``` , ```Left to Right```
       * re-print ```bot.pdf``` on ```potrait mode``` and ```all sheets``` and ```two pages per side``` , ```Right to Left``` on the other side of paper
       * bind them together:
       * ![alt text](https://github.com/nort3x/BookPrinter/blob/main/img/l2r.png)
       
       

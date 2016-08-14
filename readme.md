# fuckbdp  
  
百度盘下载工具  
  
---  
  
### Linux:  
  
```  
sudo apt-get install git aria2c  
git clone https://github.com/bieberg0n/fuckbdp.git  
cd fuckbdp/  
cp fuckbdp.json ~/.fuckbdp  
cp fuckbdp.py ~/bin/fuckbdp  
```  
  
在~/.fuckbdp中修改thread项(线程数)为8或16  
在chrome中安装"百度网盘助手",登录百度盘,勾选需要下载的文件,"导出下载"按钮中选"导出下载"-"存为aria文件",然后命令行进入含有"aria2c.down"的目录  
  
```  
fuckbdp aria2c.down  
```  
  
即可完成下载.  
  
###License (MIT)
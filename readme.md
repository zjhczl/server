# ubuntu server
## 自启动
/etc/rc.local
```
mount /dev/sda2 /mnt
nohup minio server /mnt/minio > /home/zj/server/minio/minio.log 2>&1 &
nohup sslocal -c /home/zj/server/ssr/zj.json > /home/zj/server/ssr/sslocal.log 2>&1 &
nohup /home/zj/server/frp/frpc -c /home/zj/server/frp/frpc.ini > /home/zj/server/frp/frpc.log 2>&1 &

```

# ssh反代理
```
$ ssh.exe -fN -L 12346:192.168.2.188:80 -p 8905 pegasus@10.58.32.11
```
本地的12346遂穿到10.58.32.11（8905）局域网内192.168.2.188:80

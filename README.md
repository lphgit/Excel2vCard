# Excel2vCard
convert excel data to vcard 

### what is excel

### 功能
将excel 转换为 vCard格式

### vCard 是什么

vCard, also known as VCF (Virtual Contact File), is a file format standard for electronic business cards

### how to read data from excel

python 安装 xlrd 后可以直接解析excel文件

### vCard example

> BEGIN:VCARD //开始标签
>
> VERSION:3.0 // 版本 
>
> N:张;丹丹;;; // 姓 和 名 
>
> FN:张丹丹 // 全名
>
> TEL;TYPE=CELL:136 7184 8074 // 电话
>
> ORG;CHARSET=UTF-8:公司名称  // 公司名称
>
> END:VCARD // 结束
>
>
> END:VCARD
>
> BEGIN:VCARD
>
> VERSION:3.0
>
> N:李荣杰;;;;
>
> FN:李荣杰 
>
> TEL;TYPE=CELL:158 9361 5049
>
> END:VCARD
>
> ...
>

### how to convert

vCard 模板

> BEGIN:VCARD
>
> VERSION:3.0
>
> FN:姓名
>
> TEL;TYPE=CELL:电话
>
> ORG;CHARSET=UTF-8:公司名称
>
> END:VCARD
>



只需要提取excel文件中的姓名 电话 公司名称 然后填充到vCard文件中即可。

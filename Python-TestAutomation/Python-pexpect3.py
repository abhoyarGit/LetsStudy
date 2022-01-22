import pexpect

child = pexpect.spawn('scp foo myname@host.example.com:.')
child.expect ('Password:')
child.sendline (mypassword)
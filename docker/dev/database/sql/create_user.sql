alter session set "_ORACLE_SCRIPT"=true;
create user admin identified by admin;
create user pycodebe identified by pycodebe;
grant connect, resource to pycodebe;
grant dba to admin;
exit;
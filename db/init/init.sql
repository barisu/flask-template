use template;
create table if not exists user(
    id bigint auto_increment not null primary key,
    name varchar(256),
    age tinyint unsigned
);

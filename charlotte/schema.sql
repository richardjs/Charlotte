drop table if exists feeds;
create table feeds(
	id integer primary key asc,
	url text not null,
	title text,
	displayname text
);

drop table if exists entries;
create table entries(
	id integer primary key asc,
	feedid references feeds(id),
	guid text not null,
	url text not null,
	title text
);

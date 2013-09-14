drop table if exists feeds;
create table feeds(
	id integer primary key asc,
	url text not null,
	title text,
	display_name text
);

drop table if exists entries;
create table entries(
	id integer primary key asc,
	feed_id references feeds(id),
	url text not null,
	title text not null,
	retrieved_timestamp text default CURRENT_TIMESTAMP
);

import work_with_mysql as m


def main():
    m.connect_to_mysql()
    m.create_database("online_movie_rating")
    m.show_databases()
    m.connect_database("online_movie_rating")


if __name__ == "__main__":
    main()

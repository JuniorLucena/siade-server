dataSource {
  pooled = true
  driverClassName = "com.mysql.jdbc.Driver"
  dialect = "org.hibernate.dialect.MySQL5InnoDBDialect"
}
hibernate {
    cache.use_second_level_cache = true
    cache.use_query_cache = false
    cache.region.factory_class = 'net.sf.ehcache.hibernate.EhCacheRegionFactory' // Hibernate 3
//    cache.region.factory_class = 'org.hibernate.cache.ehcache.EhCacheRegionFactory' // Hibernate 4
}

// environment specific settings
environments {
    development {
        dataSource {
            dbCreate = "create-drop" // one of 'create', 'create-drop', 'update', 'validate', ''
            url = "jdbc:mysql://localhost:3306/siade" //porta mysql = 3306
            username = "root"
            password = ""
        }
    }
    test {
        dataSource {
            dbCreate = "update" // one of 'create', 'create-drop', 'update', 'validate', ''
            url = "jdbc:mysql://localhost:3306/siade" //porta mysql = 3306
            username = "root"
            password = ""
        }
    }
    production {
        dataSource {
            dbCreate = "create" // one of 'create', 'create-drop', 'update', 'validate', ''
            url = "jdbc:mysql://localhost:3306/siade" //porta mysql = 3306
            username = "root"
            password = ""
        }
    }
}

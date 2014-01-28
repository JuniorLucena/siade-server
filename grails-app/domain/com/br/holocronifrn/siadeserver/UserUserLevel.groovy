package com.br.holocronifrn.siadeserver

import org.apache.commons.lang.builder.HashCodeBuilder

class UserUserLevel implements Serializable {

	private static final long serialVersionUID = 1

	User user
	UserLevel userLevel

	boolean equals(other) {
		if (!(other instanceof UserUserLevel)) {
			return false
		}

		other.user?.id == user?.id &&
			other.userLevel?.id == userLevel?.id
	}

	int hashCode() {
		def builder = new HashCodeBuilder()
		if (user) builder.append(user.id)
		if (userLevel) builder.append(userLevel.id)
		builder.toHashCode()
	}

	static UserUserLevel get(long userId, long userLevelId) {
		UserUserLevel.where {
			user == User.load(userId) &&
			userLevel == UserLevel.load(userLevelId)
		}.get()
	}

	static UserUserLevel create(User user, UserLevel userLevel, boolean flush = false) {
		new UserUserLevel(user: user, userLevel: userLevel).save(flush: flush, insert: true)
	}

	static boolean remove(User u, UserLevel r, boolean flush = false) {

		int rowCount = UserUserLevel.where {
			user == User.load(u.id) &&
			userLevel == UserLevel.load(r.id)
		}.deleteAll()

		rowCount > 0
	}

	static void removeAll(User u) {
		UserUserLevel.where {
			user == User.load(u.id)
		}.deleteAll()
	}

	static void removeAll(UserLevel r) {
		UserUserLevel.where {
			userLevel == UserLevel.load(r.id)
		}.deleteAll()
	}

	static mapping = {
		id composite: ['userLevel', 'user']
		version false
	}
}

package com.br.holocronifrn.siadeserver



import grails.test.mixin.*
import spock.lang.*

@TestFor(UserLevelController)
@Mock(UserLevel)
class UserLevelControllerSpec extends Specification {

    def populateValidParams(params) {
        assert params != null
        // TODO: Populate valid properties like...
        //params["name"] = 'someValidName'
    }

    void "Test the index action returns the correct model"() {

        when:"The index action is executed"
            controller.index()

        then:"The model is correct"
            !model.userLevelInstanceList
            model.userLevelInstanceCount == 0
    }

    void "Test the create action returns the correct model"() {
        when:"The create action is executed"
            controller.create()

        then:"The model is correctly created"
            model.userLevelInstance!= null
    }

    void "Test the save action correctly persists an instance"() {

        when:"The save action is executed with an invalid instance"
            def userLevel = new UserLevel()
            userLevel.validate()
            controller.save(userLevel)

        then:"The create view is rendered again with the correct model"
            model.userLevelInstance!= null
            view == 'create'

        when:"The save action is executed with a valid instance"
            response.reset()
            populateValidParams(params)
            userLevel = new UserLevel(params)

            controller.save(userLevel)

        then:"A redirect is issued to the show action"
            response.redirectedUrl == '/userLevel/show/1'
            controller.flash.message != null
            UserLevel.count() == 1
    }

    void "Test that the show action returns the correct model"() {
        when:"The show action is executed with a null domain"
            controller.show(null)

        then:"A 404 error is returned"
            response.status == 404

        when:"A domain instance is passed to the show action"
            populateValidParams(params)
            def userLevel = new UserLevel(params)
            controller.show(userLevel)

        then:"A model is populated containing the domain instance"
            model.userLevelInstance == userLevel
    }

    void "Test that the edit action returns the correct model"() {
        when:"The edit action is executed with a null domain"
            controller.edit(null)

        then:"A 404 error is returned"
            response.status == 404

        when:"A domain instance is passed to the edit action"
            populateValidParams(params)
            def userLevel = new UserLevel(params)
            controller.edit(userLevel)

        then:"A model is populated containing the domain instance"
            model.userLevelInstance == userLevel
    }

    void "Test the update action performs an update on a valid domain instance"() {
        when:"Update is called for a domain instance that doesn't exist"
            controller.update(null)

        then:"A 404 error is returned"
            response.redirectedUrl == '/userLevel/index'
            flash.message != null


        when:"An invalid domain instance is passed to the update action"
            response.reset()
            def userLevel = new UserLevel()
            userLevel.validate()
            controller.update(userLevel)

        then:"The edit view is rendered again with the invalid instance"
            view == 'edit'
            model.userLevelInstance == userLevel

        when:"A valid domain instance is passed to the update action"
            response.reset()
            populateValidParams(params)
            userLevel = new UserLevel(params).save(flush: true)
            controller.update(userLevel)

        then:"A redirect is issues to the show action"
            response.redirectedUrl == "/userLevel/show/$userLevel.id"
            flash.message != null
    }

    void "Test that the delete action deletes an instance if it exists"() {
        when:"The delete action is called for a null instance"
            controller.delete(null)

        then:"A 404 is returned"
            response.redirectedUrl == '/userLevel/index'
            flash.message != null

        when:"A domain instance is created"
            response.reset()
            populateValidParams(params)
            def userLevel = new UserLevel(params).save(flush: true)

        then:"It exists"
            UserLevel.count() == 1

        when:"The domain instance is passed to the delete action"
            controller.delete(userLevel)

        then:"The instance is deleted"
            UserLevel.count() == 0
            response.redirectedUrl == '/userLevel/index'
            flash.message != null
    }
}

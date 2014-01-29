package com.br.holocronifrn.siadeserver



import grails.test.mixin.*
import spock.lang.*

@TestFor(StateController)
@Mock(State)
class StateControllerSpec extends Specification {

    def populateValidParams(params) {
        assert params != null
        // TODO: Populate valid properties like...
        //params["name"] = 'someValidName'
    }

    void "Test the index action returns the correct model"() {

        when:"The index action is executed"
            controller.index()

        then:"The model is correct"
            !model.stateInstanceList
            model.stateInstanceCount == 0
    }

    void "Test the create action returns the correct model"() {
        when:"The create action is executed"
            controller.create()

        then:"The model is correctly created"
            model.stateInstance!= null
    }

    void "Test the save action correctly persists an instance"() {

        when:"The save action is executed with an invalid instance"
            def state = new State()
            state.validate()
            controller.save(state)

        then:"The create view is rendered again with the correct model"
            model.stateInstance!= null
            view == 'create'

        when:"The save action is executed with a valid instance"
            response.reset()
            populateValidParams(params)
            state = new State(params)

            controller.save(state)

        then:"A redirect is issued to the show action"
            response.redirectedUrl == '/state/show/1'
            controller.flash.message != null
            State.count() == 1
    }

    void "Test that the show action returns the correct model"() {
        when:"The show action is executed with a null domain"
            controller.show(null)

        then:"A 404 error is returned"
            response.status == 404

        when:"A domain instance is passed to the show action"
            populateValidParams(params)
            def state = new State(params)
            controller.show(state)

        then:"A model is populated containing the domain instance"
            model.stateInstance == state
    }

    void "Test that the edit action returns the correct model"() {
        when:"The edit action is executed with a null domain"
            controller.edit(null)

        then:"A 404 error is returned"
            response.status == 404

        when:"A domain instance is passed to the edit action"
            populateValidParams(params)
            def state = new State(params)
            controller.edit(state)

        then:"A model is populated containing the domain instance"
            model.stateInstance == state
    }

    void "Test the update action performs an update on a valid domain instance"() {
        when:"Update is called for a domain instance that doesn't exist"
            controller.update(null)

        then:"A 404 error is returned"
            response.redirectedUrl == '/state/index'
            flash.message != null


        when:"An invalid domain instance is passed to the update action"
            response.reset()
            def state = new State()
            state.validate()
            controller.update(state)

        then:"The edit view is rendered again with the invalid instance"
            view == 'edit'
            model.stateInstance == state

        when:"A valid domain instance is passed to the update action"
            response.reset()
            populateValidParams(params)
            state = new State(params).save(flush: true)
            controller.update(state)

        then:"A redirect is issues to the show action"
            response.redirectedUrl == "/state/show/$state.id"
            flash.message != null
    }

    void "Test that the delete action deletes an instance if it exists"() {
        when:"The delete action is called for a null instance"
            controller.delete(null)

        then:"A 404 is returned"
            response.redirectedUrl == '/state/index'
            flash.message != null

        when:"A domain instance is created"
            response.reset()
            populateValidParams(params)
            def state = new State(params).save(flush: true)

        then:"It exists"
            State.count() == 1

        when:"The domain instance is passed to the delete action"
            controller.delete(state)

        then:"The instance is deleted"
            State.count() == 0
            response.redirectedUrl == '/state/index'
            flash.message != null
    }
}

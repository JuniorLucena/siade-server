package siade.server

import grails.transaction.Transactional

import com.google.android.gcm.server.Message
import com.google.android.gcm.server.Result
import com.google.android.gcm.server.Sender

@Transactional
class SendMessageService {

	/**
	 *  Variável com o ID do dispositivo registrado no GCM.
	 *  Por enquanto e um id estatico mais futuramente deve ser recuperado pelo banco,
	 *  pois cada device tera um id, que sera registrado
	 */
	final String ID_DISPOSITIVO_GCM = "APA91bFddY7603ATintCpr6WJv6OQrEg8_-CDy1zFxEieFCWqtNvESPU6oNOeaG2QPFVN1GO6kJhVUMrZHmISdsPF9LF_5qyS9I6IT1reZmDC5kuQNXYEdiubQTQCxb8sb7WI8xkR7NFs6AtllbBtAgl5-7Yi8kF2A";
	// Variável com a chave obtida em API ACCESS no Google APIs
	final String API_KEY = "AIzaSyDr8V_tQi6rJ0TyvMN32KGRuakGj6tiPw8";

	final String ID_MESSAGE = "mensagem"

	def sendMessage(String json) {

		/**
		 * ID do Sender (Enviador)
		 */
		def sender = new Sender(API_KEY)

		def message = new Message.Builder()	.collapseKey("1")
				.timeToLive(3)
				.delayWhileIdle(true)
				.addData(ID_MESSAGE, // identificador da mensagem
				json)
				.build();

		Result result = null

		/**
		 * Envia a mensagem para o dispositivo
		 */
		try {
			result = sender.send(message,ID_DISPOSITIVO_GCM, 1);
		} catch (IOException e) {
			e.printStackTrace()
			println "Falha na conexão! Tente se conectar a internet!"
		}

		// Imprime o resultado do envio na saída padrão
		if (result != null)
			println result.toString()

	}
}

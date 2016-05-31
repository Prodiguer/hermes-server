# -*- coding: utf-8 -*-

"""
.. module:: hermes.mq.constants.py
   :platform: Unix
   :synopsis: Hermes mq constants.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
# AMPQ message exchange types.
AMPQ_EXCHANGE_TYPE_DIRECT = "direct"
AMPQ_EXCHANGE_TYPE_FANOUT = "fanout"
AMPQ_EXCHANGE_TYPE_HEADER = "header"
AMPQ_EXCHANGE_TYPE_TOPIC = "topic"

# All AMPQ exchange types.
AMPQ_EXCHANGE_TYPES = {
	AMPQ_EXCHANGE_TYPE_DIRECT,
	AMPQ_EXCHANGE_TYPE_FANOUT,
	AMPQ_EXCHANGE_TYPE_HEADER,
	AMPQ_EXCHANGE_TYPE_TOPIC
	}

# AMPQ message delivery modes.
AMPQ_DELIVERY_MODE_NON_PERSISTENT = 1
AMPQ_DELIVERY_MODE_PERSISTENT = 2

# All AMPQ message delivery modes.
AMPQ_DELIVERY_MODES = {
	AMPQ_DELIVERY_MODE_NON_PERSISTENT,
	AMPQ_DELIVERY_MODE_PERSISTENT
	}

# Message server virtual host.
VHOST = "hermes"

# Message server exchanges.
EXCHANGE_HERMES_PRIMARY = "x-primary"
EXCHANGE_HERMES_SECONDARY = "x-secondary"
EXCHANGE_HERMES_SECONDARY_DELAYED = "x-secondary-delayed"

# All exchanges.
EXCHANGES = {
	EXCHANGE_HERMES_PRIMARY,
	EXCHANGE_HERMES_SECONDARY,
	EXCHANGE_HERMES_SECONDARY_DELAYED
	}

# Live message queues.
QUEUE_LIVE_ALERT = 'live-alert'
QUEUE_LIVE_CV = 'live-cv'
QUEUE_LIVE_FE = 'live-fe'
QUEUE_LIVE_METRICS = 'live-metrics'
QUEUE_LIVE_METRICS_PCMDI = 'live-metrics-pcmdi'
QUEUE_LIVE_MONITORING_COMPUTE = "live-monitoring-compute"
QUEUE_LIVE_MONITORING_POST_PROCESSING = "live-monitoring-post-processing"
QUEUE_LIVE_SMTP = 'live-smtp'
QUEUE_LIVE_SUPERVISEUR = 'live-superviseur'

# Debug message queues.
QUEUE_DEBUG_0000 = 'debug-0000'
QUEUE_DEBUG_0100 = 'debug-0100'
QUEUE_DEBUG_1000 = 'debug-1000'
QUEUE_DEBUG_1100 = 'debug-1100'
QUEUE_DEBUG_1900 = 'debug-1900'
QUEUE_DEBUG_1999 = 'debug-1999'
QUEUE_DEBUG_2000 = 'debug-2000'
QUEUE_DEBUG_2100 = 'debug-2100'
QUEUE_DEBUG_2900 = 'debug-2900'
QUEUE_DEBUG_2999 = 'debug-2999'
QUEUE_DEBUG_3000 = 'debug-3000'
QUEUE_DEBUG_3100 = 'debug-3100'
QUEUE_DEBUG_3900 = 'debug-3900'
QUEUE_DEBUG_3999 = 'debug-3999'
QUEUE_DEBUG_7000 = 'debug-7000'
QUEUE_DEBUG_7010 = 'debug-7010'
QUEUE_DEBUG_7100 = 'debug-7100'
QUEUE_DEBUG_8000 = 'debug-8000'
QUEUE_DEBUG_8100 = 'debug-8100'
QUEUE_DEBUG_8200 = 'debug-8200'
QUEUE_DEBUG_8888 = 'debug-8888'
QUEUE_DEBUG_ALERT = 'debug-alert'
QUEUE_DEBUG_CV = 'debug-cv'
QUEUE_DEBUG_FE = 'debug-fe'
QUEUE_DEBUG_SMTP = 'debug-smtp'

# All queues.
QUEUES = {
	# Live queues.
	QUEUE_LIVE_ALERT,
	QUEUE_LIVE_CV,
	QUEUE_LIVE_FE,
	QUEUE_LIVE_METRICS,
	QUEUE_LIVE_METRICS_PCMDI,
	QUEUE_LIVE_MONITORING_COMPUTE,
	QUEUE_LIVE_MONITORING_POST_PROCESSING,
	QUEUE_LIVE_SMTP,
	QUEUE_LIVE_SUPERVISEUR,
	# Debug queues.
	QUEUE_DEBUG_0000,
	QUEUE_DEBUG_0100,
	QUEUE_DEBUG_1000,
	QUEUE_DEBUG_1100,
	QUEUE_DEBUG_1900,
	QUEUE_DEBUG_1999,
	QUEUE_DEBUG_2000,
	QUEUE_DEBUG_2100,
	QUEUE_DEBUG_2900,
	QUEUE_DEBUG_2999,
	QUEUE_DEBUG_3000,
	QUEUE_DEBUG_3100,
	QUEUE_DEBUG_3900,
	QUEUE_DEBUG_3999,
	QUEUE_DEBUG_7000,
	QUEUE_DEBUG_7010,
	QUEUE_DEBUG_7100,
	QUEUE_DEBUG_8000,
	QUEUE_DEBUG_8100,
	QUEUE_DEBUG_8200,
	QUEUE_DEBUG_8888,
	QUEUE_DEBUG_ALERT,
	QUEUE_DEBUG_CV,
	QUEUE_DEBUG_FE,
	QUEUE_DEBUG_SMTP
	}

# Message producers.
PRODUCER_IGCM = u"libigcm"
PRODUCER_HERMES = u"hermes"

# All producers.
PRODUCERS = {
	PRODUCER_IGCM,
	PRODUCER_HERMES
	}

# Message server users.
USER_HERMES = u"hermes-mq-user"
USER_HERMES_ADMIN = u"hermes-mq-admin"

# All users.
USERS = {
	USER_HERMES,
	USER_HERMES_ADMIN
	}

# Message application identifiers.
APP_INTERNAL = u"internal"
APP_MONITORING = u"monitoring"
APP_METRICS = u"metrics"
APP_SUPERVISEUR = u"superviseur"

# All apps.
APPS = {
	APP_INTERNAL,
	APP_METRICS,
	APP_MONITORING,
	APP_SUPERVISEUR
	}

# Message types:
# ... general message types.
MESSAGE_TYPE_0000 = u"0000"		# Monitoring - simulation initialiation
MESSAGE_TYPE_0100 = u"0100"		# Monitoring - simulation ends
MESSAGE_TYPE_1000 = u"1000"		# Monitoring - computing job begins
MESSAGE_TYPE_1100 = u"1100"		# Monitoring - computing job ends
MESSAGE_TYPE_1900 = u"1900"		# Monitoring - computing job command failure
MESSAGE_TYPE_1999 = u"1999"		# Monitoring - computing job fails - FATAL simulation has been stopped due to an error
MESSAGE_TYPE_2000 = u"2000"		# Monitoring - post-processing job begins
MESSAGE_TYPE_2100 = u"2100"		# Monitoring - post-processing job ends
MESSAGE_TYPE_2900 = u"2900"		# Monitoring - post-processing command failure
MESSAGE_TYPE_2999 = u"2999"		# Monitoring - post-processing job fails - FATAL post-processing has been stopped due to an error
MESSAGE_TYPE_3000 = u"3000"		# Monitoring - post-processing job from checker begins
MESSAGE_TYPE_3100 = u"3100"		# Monitoring - post-processing job from checker ends
MESSAGE_TYPE_3900 = u"3900"		# Monitoring - post-processing job from checker fails
MESSAGE_TYPE_3999 = u"3999"		# Monitoring - post-processing-from0checker job fails - FATAL post-processing from checker has been stopped due to an error
MESSAGE_TYPE_7000 = u"7000"		# Metrics - environment
MESSAGE_TYPE_7010 = u"7010"		# Metrics - conso
MESSAGE_TYPE_7011 = u"7010"		# Metrics - conso
MESSAGE_TYPE_7100 = u"7100"		# Metrics - pcmdi
MESSAGE_TYPE_8000 = u"8000"		# Supervisor - detect
MESSAGE_TYPE_8100 = u"8100"		# Supervisor - format
MESSAGE_TYPE_8200 = u"8200"		# Supervisor - dispatch
MESSAGE_TYPE_8888 = u"8888"		# Misc - cleanup
MESSAGE_TYPE_CV = u"-1000"		# Internal - controlled vocabulary
MESSAGE_TYPE_FE = u"-2000"		# Internal - front end notifications
MESSAGE_TYPE_SMTP = u"-3000"	# Internal - smtp inputs
MESSAGE_TYPE_ALERT = u"-4000"	# Internal - operator alerts


# All types.
TYPES = {
	# ... monitoring - simulation
	MESSAGE_TYPE_0000,
	MESSAGE_TYPE_0100,
	# ... monitoring - compute jobs
	MESSAGE_TYPE_1000,
	MESSAGE_TYPE_1100,
	MESSAGE_TYPE_1900,
	MESSAGE_TYPE_1999,
	# ... monitoring - post-processing jobs
	MESSAGE_TYPE_2000,
	MESSAGE_TYPE_2100,
	MESSAGE_TYPE_2900,
	MESSAGE_TYPE_2999,
	# ... monitoring - post-processing from checker jobs
	MESSAGE_TYPE_3000,
	MESSAGE_TYPE_3100,
	MESSAGE_TYPE_3900,
	MESSAGE_TYPE_3999,
	# ... metrics
	MESSAGE_TYPE_7000,
	MESSAGE_TYPE_7010,
	MESSAGE_TYPE_7011,
	MESSAGE_TYPE_7100,
	# ... supervisor
	MESSAGE_TYPE_8000,
	MESSAGE_TYPE_8100,
	MESSAGE_TYPE_8200,
	# ... misc
	MESSAGE_TYPE_8888,
	# ... internal
	MESSAGE_TYPE_FE,
	MESSAGE_TYPE_CV,
	MESSAGE_TYPE_SMTP,
	MESSAGE_TYPE_ALERT
	}

# Map of applications to message types.
MESSAGE_TYPE_APPLICATION = {
	# ... monitoring - simulation
	MESSAGE_TYPE_0000: APP_MONITORING,
	MESSAGE_TYPE_0100: APP_MONITORING,
	# ... monitoring - compute jobs
	MESSAGE_TYPE_1000: APP_MONITORING,
	MESSAGE_TYPE_1100: APP_MONITORING,
	MESSAGE_TYPE_1900: APP_MONITORING,
	MESSAGE_TYPE_1999: APP_MONITORING,
	# ... monitoring - post-processing jobs
	MESSAGE_TYPE_2000: APP_MONITORING,
	MESSAGE_TYPE_2100: APP_MONITORING,
	MESSAGE_TYPE_2900: APP_MONITORING,
	MESSAGE_TYPE_2999: APP_MONITORING,
	# ... monitoring - post-processing from checker jobs
	MESSAGE_TYPE_3000: APP_MONITORING,
	MESSAGE_TYPE_3100: APP_MONITORING,
	MESSAGE_TYPE_3900: APP_MONITORING,
	MESSAGE_TYPE_3999: APP_MONITORING,
	# ... metrics
	MESSAGE_TYPE_7000: APP_METRICS,
	MESSAGE_TYPE_7010: APP_METRICS,
	MESSAGE_TYPE_7011: APP_METRICS,
	MESSAGE_TYPE_7100: APP_METRICS,
	# ... supervisor
	MESSAGE_TYPE_8000: APP_SUPERVISEUR,
	MESSAGE_TYPE_8100: APP_SUPERVISEUR,
	MESSAGE_TYPE_8200: APP_SUPERVISEUR,
	# ... misc
	MESSAGE_TYPE_8888: APP_MONITORING,
	# ... other
	MESSAGE_TYPE_FE: APP_INTERNAL,
	MESSAGE_TYPE_CV: APP_INTERNAL,
	MESSAGE_TYPE_SMTP: APP_INTERNAL,
	MESSAGE_TYPE_ALERT: APP_INTERNAL
	}

# Map of exchanges to message types.
MESSAGE_TYPE_EXCHANGE = {
	# ... monitoring - simulation
	MESSAGE_TYPE_0000: EXCHANGE_HERMES_PRIMARY,
	MESSAGE_TYPE_0100: EXCHANGE_HERMES_PRIMARY,
	# ... monitoring - compute jobs
	MESSAGE_TYPE_1000: EXCHANGE_HERMES_PRIMARY,
	MESSAGE_TYPE_1100: EXCHANGE_HERMES_PRIMARY,
	MESSAGE_TYPE_1900: EXCHANGE_HERMES_PRIMARY,
	MESSAGE_TYPE_1999: EXCHANGE_HERMES_PRIMARY,
	# ... monitoring - post-processing jobs
	MESSAGE_TYPE_2000: EXCHANGE_HERMES_PRIMARY,
	MESSAGE_TYPE_2100: EXCHANGE_HERMES_PRIMARY,
	MESSAGE_TYPE_2900: EXCHANGE_HERMES_PRIMARY,
	MESSAGE_TYPE_2999: EXCHANGE_HERMES_PRIMARY,
	# ... monitoring - post-processing from checker jobs
	MESSAGE_TYPE_3000: EXCHANGE_HERMES_PRIMARY,
	MESSAGE_TYPE_3100: EXCHANGE_HERMES_PRIMARY,
	MESSAGE_TYPE_3900: EXCHANGE_HERMES_PRIMARY,
	MESSAGE_TYPE_3999: EXCHANGE_HERMES_PRIMARY,
	# ... metrics
	MESSAGE_TYPE_7000: EXCHANGE_HERMES_PRIMARY,
	MESSAGE_TYPE_7010: EXCHANGE_HERMES_PRIMARY,
	MESSAGE_TYPE_7011: EXCHANGE_HERMES_PRIMARY,
	MESSAGE_TYPE_7100: EXCHANGE_HERMES_PRIMARY,
	# ... supervisor
	MESSAGE_TYPE_8000: EXCHANGE_HERMES_SECONDARY_DELAYED,
	MESSAGE_TYPE_8100: EXCHANGE_HERMES_SECONDARY,
	MESSAGE_TYPE_8200: EXCHANGE_HERMES_SECONDARY,
	# ... misc
	MESSAGE_TYPE_8888: EXCHANGE_HERMES_PRIMARY,
	# ... other
	MESSAGE_TYPE_FE: EXCHANGE_HERMES_SECONDARY,
	MESSAGE_TYPE_CV: EXCHANGE_HERMES_SECONDARY,
	MESSAGE_TYPE_SMTP: EXCHANGE_HERMES_SECONDARY,
	MESSAGE_TYPE_ALERT: EXCHANGE_HERMES_SECONDARY
	}

# Timestamp precision types.
TIMESTAMP_PRECISION_NS = u"ns"
TIMESTAMP_PRECISION_MS = u"ms"

# All timestamp precision types.
TIMESTAMP_PRECISIONS = {
	TIMESTAMP_PRECISION_NS,
	TIMESTAMP_PRECISION_MS
	}

# Content types.
CONTENT_TYPE_JSON = 'application/json'
CONTENT_TYPE_BASE64 = 'application/base64'
CONTENT_TYPE_BASE64_JSON = 'application/base64+json'

# All content types.
CONTENT_TYPES = {
	CONTENT_TYPE_JSON,
	CONTENT_TYPE_BASE64,
	CONTENT_TYPE_BASE64_JSON,
	}

# Content encodings.
CONTENT_ENCODING_UNICODE = "utf-8"

# All content encodings.
CONTENT_ENCODINGS = {
	CONTENT_ENCODING_UNICODE
	}

# Message priorities.
PRIORITY_LOW = 1
PRIORITY_NORMAL = 4
PRIORITY_HIGH = 7
PRIORITY_URGENT = 9
PRIORITY_CRITICAL = 10

# All message priorities.
PRIORITIES = {
	PRIORITY_LOW,
	PRIORITY_NORMAL,
	PRIORITY_HIGH,
	PRIORITY_URGENT,
	PRIORITY_CRITICAL,
	}


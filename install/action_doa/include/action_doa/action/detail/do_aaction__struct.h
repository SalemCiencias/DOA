// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from action_doa:action/DOAaction.idl
// generated code does not contain a copyright notice

#ifndef ACTION_DOA__ACTION__DETAIL__DO_AACTION__STRUCT_H_
#define ACTION_DOA__ACTION__DETAIL__DO_AACTION__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Struct defined in action/DOAaction in the package action_doa.
typedef struct action_doa__action__DOAaction_Goal
{
  int32_t orden;
} action_doa__action__DOAaction_Goal;

// Struct for a sequence of action_doa__action__DOAaction_Goal.
typedef struct action_doa__action__DOAaction_Goal__Sequence
{
  action_doa__action__DOAaction_Goal * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} action_doa__action__DOAaction_Goal__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'resultado'
#include "rosidl_runtime_c/string.h"

// Struct defined in action/DOAaction in the package action_doa.
typedef struct action_doa__action__DOAaction_Result
{
  rosidl_runtime_c__String resultado;
} action_doa__action__DOAaction_Result;

// Struct for a sequence of action_doa__action__DOAaction_Result.
typedef struct action_doa__action__DOAaction_Result__Sequence
{
  action_doa__action__DOAaction_Result * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} action_doa__action__DOAaction_Result__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'feedback'
// already included above
// #include "rosidl_runtime_c/string.h"

// Struct defined in action/DOAaction in the package action_doa.
typedef struct action_doa__action__DOAaction_Feedback
{
  rosidl_runtime_c__String feedback;
} action_doa__action__DOAaction_Feedback;

// Struct for a sequence of action_doa__action__DOAaction_Feedback.
typedef struct action_doa__action__DOAaction_Feedback__Sequence
{
  action_doa__action__DOAaction_Feedback * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} action_doa__action__DOAaction_Feedback__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
#include "unique_identifier_msgs/msg/detail/uuid__struct.h"
// Member 'goal'
#include "action_doa/action/detail/do_aaction__struct.h"

// Struct defined in action/DOAaction in the package action_doa.
typedef struct action_doa__action__DOAaction_SendGoal_Request
{
  unique_identifier_msgs__msg__UUID goal_id;
  action_doa__action__DOAaction_Goal goal;
} action_doa__action__DOAaction_SendGoal_Request;

// Struct for a sequence of action_doa__action__DOAaction_SendGoal_Request.
typedef struct action_doa__action__DOAaction_SendGoal_Request__Sequence
{
  action_doa__action__DOAaction_SendGoal_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} action_doa__action__DOAaction_SendGoal_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'stamp'
#include "builtin_interfaces/msg/detail/time__struct.h"

// Struct defined in action/DOAaction in the package action_doa.
typedef struct action_doa__action__DOAaction_SendGoal_Response
{
  bool accepted;
  builtin_interfaces__msg__Time stamp;
} action_doa__action__DOAaction_SendGoal_Response;

// Struct for a sequence of action_doa__action__DOAaction_SendGoal_Response.
typedef struct action_doa__action__DOAaction_SendGoal_Response__Sequence
{
  action_doa__action__DOAaction_SendGoal_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} action_doa__action__DOAaction_SendGoal_Response__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__struct.h"

// Struct defined in action/DOAaction in the package action_doa.
typedef struct action_doa__action__DOAaction_GetResult_Request
{
  unique_identifier_msgs__msg__UUID goal_id;
} action_doa__action__DOAaction_GetResult_Request;

// Struct for a sequence of action_doa__action__DOAaction_GetResult_Request.
typedef struct action_doa__action__DOAaction_GetResult_Request__Sequence
{
  action_doa__action__DOAaction_GetResult_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} action_doa__action__DOAaction_GetResult_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'result'
// already included above
// #include "action_doa/action/detail/do_aaction__struct.h"

// Struct defined in action/DOAaction in the package action_doa.
typedef struct action_doa__action__DOAaction_GetResult_Response
{
  int8_t status;
  action_doa__action__DOAaction_Result result;
} action_doa__action__DOAaction_GetResult_Response;

// Struct for a sequence of action_doa__action__DOAaction_GetResult_Response.
typedef struct action_doa__action__DOAaction_GetResult_Response__Sequence
{
  action_doa__action__DOAaction_GetResult_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} action_doa__action__DOAaction_GetResult_Response__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__struct.h"
// Member 'feedback'
// already included above
// #include "action_doa/action/detail/do_aaction__struct.h"

// Struct defined in action/DOAaction in the package action_doa.
typedef struct action_doa__action__DOAaction_FeedbackMessage
{
  unique_identifier_msgs__msg__UUID goal_id;
  action_doa__action__DOAaction_Feedback feedback;
} action_doa__action__DOAaction_FeedbackMessage;

// Struct for a sequence of action_doa__action__DOAaction_FeedbackMessage.
typedef struct action_doa__action__DOAaction_FeedbackMessage__Sequence
{
  action_doa__action__DOAaction_FeedbackMessage * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} action_doa__action__DOAaction_FeedbackMessage__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // ACTION_DOA__ACTION__DETAIL__DO_AACTION__STRUCT_H_

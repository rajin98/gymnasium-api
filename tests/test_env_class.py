from gym_http_server import Envs

def test_reset():
  e = Envs()
  id = e.create('CartPole-v1')
  original = e.get_observation_space_info(id)
  e.reset(id)
  assert original == e.get_observation_space_info(id)


def test_step():
  e = Envs()
  id = e.create('CartPole-v1')
  e.reset(id)
  retval = e.step(id,e.get_action_space_sample(id),False)
  assert retval
